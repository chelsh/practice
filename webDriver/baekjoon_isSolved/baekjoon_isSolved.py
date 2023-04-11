from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import config

URL = "https://www.acmicpc.net/login"

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)

driver.get(URL)
time.sleep(1)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Chelsh/webDriver/baekjoon_isSolved/screenshot/beforelogin.png")

input_id = driver.find_element(By.NAME, "login_user_id")
input_pw = driver.find_element(By.NAME, "login_password")

input_id.send_keys(config.ID)
input_pw.send_keys(config.PW)

login_btn = driver.find_element(By.ID, "submit_button")
login_btn.click()

time.sleep(1)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Chelsh/webDriver/baekjoon_isSolved/screenshot/afterlogin.png")

#중단 - reCAPTCHA 