from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from bardapi import Bard
import os

def generate_posts_out():
    
    
    token = 'dQi-99vJOWvTZad5TylVqU9WBXo7RPBcHwTPoDf5q8TjKGAYUoD11LriDjCD9qgVfkVmsw.'
    bard = Bard(token=token)

    chrome_driver_path = 'C:/chromedriver.exe' 
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:/Users/sujal/AppData/Local/Google/Chrome/User Data")
    options.add_argument(r'--profile-directory=Default')
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu') 
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--no-sandbox')
    options.add_argument('log-level=3')
    options.add_argument('--allow-insecure-localhost')  
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    wait = WebDriverWait(driver, 10)

    target_url='https://www.linkedin.com/feed/'
    driver.get(target_url)

    show_more=driver.find_element(By.CSS_SELECTOR,'.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view.news-module__toggle-storylines')
    show_more.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.news-module__headline.t-14.t-bold.t-black.truncate.mt1.pr4')))
    news_headlines = driver.find_elements(By.CSS_SELECTOR, '.news-module__headline.t-14.t-bold.t-black.truncate.mt1.pr4')
    news_headlines.pop(0)

    headlines=[]
    for news in news_headlines:
        if len(headlines)==5:
            break
        else:
            headlines.append(news.text)

    outputs={}

    prompt_head='Write a linkedin post about '
    prompt_foot=' in around 200 words .Do not give me any information about procedures and service features that are not mentioned in the PROVIDED CONTEXT'
            
    for news in headlines:
        prompt=prompt_head+news+prompt_foot
        output=bard.get_answer(prompt)['content']


        outputs[prompt]=output
    return outputs


