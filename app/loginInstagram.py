from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from json import load,dump
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import os
s = Service("../bin/driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.instagram.com/')
time.sleep(50)
getTkCookies = driver.get_cookies()
with open('../bin/cookies/ig.json', 'w') as file:
    dump(getTkCookies, file)
    file.close()

