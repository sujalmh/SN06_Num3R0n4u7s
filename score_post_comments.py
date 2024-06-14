from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from transformers import AutoModelForSequenceClassification, pipeline
from transformers import AutoTokenizer, AutoConfig
from scipy.special import softmax

MODEL = f"C:/Users/sujal/cardiffnlp/twitter-xlm-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

config = AutoConfig.from_pretrained(MODEL)
config.save_pretrained(MODEL)

tokenizer.save_pretrained(MODEL)
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)

def summarize(text):
    return summarizer(text, max_length=100, min_length=15, do_sample=False)

def result_post_comments(target_url):
    chrome_driver_path = 'C:/chromedriver.exe' 
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:/Users/sujal/AppData/Local/Google/Chrome/User Data") #Profile path
    options.add_argument(r'--profile-directory=Default')
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu') 
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--no-sandbox')
    options.add_argument('log-level=3')
    options.add_argument('--allow-insecure-localhost')  
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


    # Set up the web driver (make sure you have the appropriate driver installed)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    # Navigate to the URL
    driver.get(target_url)

    post_element=driver.find_element(By.XPATH,'//div/div[4]/div/div/span/span')
    post=post_element.get_attribute("textContent")

    # Define the target element class
    target_element_class = ".mv3.mr3.ml4.t-14.t-black--light"

    # Function to check if the target element is present
    def is_target_element_present():
        try:
            driver.find_element(By.CSS_SELECTOR, target_element_class)
            return True
        except:
            return False

    # Loop to click the button until the target element is found
    while not is_target_element_present():
        # Replace "comments-comments-list__load-more-comments-button" with the actual class of your button
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "comments-comments-list__load-more-comments-button"))
            )
            load_more_button.click()
        except:
            break
    # Perform actions with the found target element if needed
    spans = driver.find_elements(By.XPATH, '//div/div/span/div/span')
    comments=[]
    for span in spans:
        parent_text = span.get_attribute("textContent")
        parent_text = parent_text.split('hashtag', 1)[0].strip()
        parent_text = parent_text.split('https', 1)[0].strip() 
        parent_text = parent_text.split('•', 1)[0].strip()
        comments.append(parent_text)
    driver.quit()

    comments_pos=""
    comments_neu=""
    comments_neg=""
    comments_pos_count=0
    comments_neg_count=0
    comments_neu_count=0

    post_id=0

    for text in comments:                                                                  #score
        text+=" "
        post_id+=1
        if len(text)<3:
            continue
        else:
            try:
                encoded_input = tokenizer(text, return_tensors='pt')
                output = model(**encoded_input)
                score_positive = output[0][0].detach().numpy()
                score_positive = softmax(score_positive)
                score_positive.tolist()
                pos_score=score_positive[2]
                neu_score=score_positive[1]
                neg_score=score_positive[0]

                if pos_score>neg_score and pos_score>neu_score:
                    comments_pos+=text
                    comments_pos_count+=1
                if neg_score>pos_score and neg_score>neu_score:
                    comments_neg+=text
                    comments_neg_count+=1
                if neu_score>pos_score and neu_score>neg_score:
                    comments_neu+=text
                    comments_neu_count+=1
            except:
                continue

    total=comments_neg_count+comments_pos_count
    per_pos=round((comments_pos_count/total),2)
            
    summ_pos=summarize(comments_pos)[0]['summary_text']
    summ_neu=summarize(comments_neu)[0]['summary_text']
    summ_neg=summarize(comments_neg)[0]['summary_text']
    return post, summ_pos, summ_neu, summ_neg, per_pos

