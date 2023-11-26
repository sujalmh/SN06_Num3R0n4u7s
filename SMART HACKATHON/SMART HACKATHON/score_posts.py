from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    options.add_argument(r"--user-data-dir=C:/Users/sujal/AppData/Local/Google/Chrome/User Data") #Profile path
    options.add_argument(r'--profile-directory=Default') #Profile 4
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--no-sandbox')
    options.add_argument('log-level=3')
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

    posts=[]
    flag_=driver.find_element_by_xpath('.//span[@dir="ltr"]')
    flag=flag_.get_attribute("textContent")
    name=flag[0:int(len(flag)/2)]
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
        posts.append(post)    

    driver.quit()
    
    post_score_positive=[]
    post_score_emotion=[]
    final_score_positive=int()
    post_id=0
    final_sorted_emotions={}

    for text in posts:                                                                  #score
        post_id+=1
        try:
            encoded_input = tokenizer(text.strip(), return_tensors='pt')
            output = model(**encoded_input)
            score_positive = output[0][0].detach().numpy()
            score_positive = softmax(score_positive)
            score_positive.tolist()
            post_score=score_positive[2]-score_positive[0]
            post_score+=1
            post_score=post_score/2
            post_score=post_score*10
            post_score=round(post_score,1)
            final_score_positive+=post_score
            post_score_positive.append(post_score)
            post_emotion=classifier(text)[0]['label']
            try:
                final_sorted_emotions[post_emotion]+=1
            except:
                final_sorted_emotions[post_emotion]=1
            post_score_emotion.append(post_emotion)
        except:
            continue
    final_score_positive=final_score_positive/(post_id+1)
    final_score_positive=round(final_score_positive,1)
    return posts,post_score_positive,post_score_emotion,final_sorted_emotions,final_score_positive,name,img_url