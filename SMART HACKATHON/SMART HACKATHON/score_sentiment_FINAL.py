from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from transformers import AutoModelForSequenceClassification, pipeline
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

MODEL = f"C:/Users/sujal/cardiffnlp/twitter-xlm-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

config = AutoConfig.from_pretrained(MODEL)
config.save_pretrained(MODEL)

tokenizer.save_pretrained(MODEL)
classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")

model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)


def results(target_url,no_of_posts):
    print(target_url)
    chrome_driver_path = 'C:/chromedriver.exe' 
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu') 
    options.add_argument(r"--user-data-dir=C:/Users/sujal/AppData/Local/Google/Chrome/User Data") #Profile path
    options.add_argument(r'--profile-directory=Default') #Profile 4
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--no-sandbox')
    options.add_argument('--allow-insecure-localhost')  
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    driver.get(target_url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    
    img=driver.find_element_by_class_name('pv-top-card-profile-picture__image')
    img_url=img.get_attribute("src")

    if target_url[-1]=="/":
        target_url+='recent-activity/all/'
    else:
        target_url+='/recent-activity/all/'

    driver.get(target_url)

    count=[]
    posts_container = []
    no_of_posts=200
    while len(posts_container)<no_of_posts:  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        posts_container = driver.find_elements_by_class_name('profile-creator-shared-feed-update__container')
        count.append(len(posts_container))
        try: 
            if count[iter]==count[iter-4]:
                break
        except:
            continue
        driver.implicitly_wait(10)
        time.sleep(1)


    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)

    posts=[]
    flag_=driver.find_element_by_xpath('.//span[@dir="ltr"]')
    flag=flag_.get_attribute("textContent")
    for container in posts_container:
        spans=container.find_elements_by_xpath('.//span[@dir="ltr"]')
        
        post=""
        for span in spans:
            parent_text = span.get_attribute("textContent")
            if parent_text==flag:
                continue
            else:
                parent_text = parent_text.split('hashtag', 1)[0].strip()
                parent_text = parent_text.split('https', 1)[0].strip() 
                parent_text = parent_text.split('•', 1)[0].strip()
                post+=parent_text
        try:
            posts.append(post)
        except:
            pass      
        posts.append(post)    

    driver.quit()
    
    posts_to_remove=[]                                                                  #preprocessing
    for raw_id in range(len(posts)):
        if len(posts[raw_id])<5:
            posts_to_remove.append(raw_id)
    posts = [posts[i] for i in range(len(posts)) if i not in posts_to_remove]

    post_score_positive=dict()
    post_score_emotion=dict()
    final_score_postive=int()
    post_id=0
    final_sorted_emotions={}

    for text in posts:                                                                  #score
        post_id+=1
        if len(text)<5:
            continue
        else:
            try:
                encoded_input = tokenizer(text.strip(), return_tensors='pt')
                output = model(**encoded_input)
                score_positive = output[0][0].detach().numpy()
                score_positive = softmax(score_positive)
                score_positive.tolist()
                post_score=score_positive[2]-score_positive[0]
                final_score_postive+=post_score
                post_score_positive[post_id]=post_score
                post_emotion=classifier(text)[0]['label']
                try:
                    final_sorted_emotions[post_emotion]+=1
                except:
                    final_sorted_emotions[post_emotion]=1
                post_score_emotion[post_id]=post_emotion
            except:
                continue
    final_score_postive=final_score_postive/(post_id+1)
    return posts,post_score_positive,post_score_emotion,final_sorted_emotions,final_score_postive,img_url