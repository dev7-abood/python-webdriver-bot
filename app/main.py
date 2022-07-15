from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from json import load,dump
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import os
from collections import Counter

config = dotenv_values(".env")
s = Service("../bin/driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://getlike.io/en/login/')
if os.stat('../bin/cookies/getlike.json').st_size == 0:
    driver.find_element('id', 'User_loginLogin').send_keys(config.get('EMAIL'))
    driver.find_element('id', 'User_passwordLogin').send_keys(config.get('PASSWORD'))
    time.sleep(5)
    driver.find_element('name', 'submitLogin').click()
    time.sleep(5)
    getLinkCookies = driver.get_cookies()
    time.sleep(5)

    with open('../bin/cookies/getlike.json', 'w') as file:
        dump(getLinkCookies, file)
        file.close()
else:
    with open('../bin/cookies/getlike.json', 'r') as file:
        for index in load(file):
            driver.add_cookie(index)
            time.sleep(5)
        driver.refresh()
time.sleep(4)


driver.get('https://getlike.io/en/tasks/instagram/subscribe/')
time.sleep(5)
driver.refresh()
articles = driver.find_elements(By.TAG_NAME, 'article')
lenArticles = len(articles)

for i in range(0, lenArticles+1):
    driver.execute_script(f"document.getElementsByClassName('do do-task btn btn-sm btn-primary btn-block')[{i}].click()")
    time.sleep(10)

    try:
        handle = driver.window_handles[1]
        driver.switch_to.window(handle)

        with open('../bin/cookies/ig.json', 'r') as file:
            for index in load(file):
                driver.add_cookie(index)
            time.sleep(2)
            driver.refresh()
    finally:
        continue

# for index,i in articles:
#     print(index)
#     # i.find_element(By.CLASS_NAME, 'do do-task btn btn-sm btn-primary btn-block')
#     # driver.execute_script('window.alert("worked!")')
#     # i.click()
#     # time.sleep(10)
