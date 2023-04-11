import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import config

option_list = ['--headless', '--no-sandbox']
specific_options = webdriver.ChromeOptions()
for i in option_list:
    specific_options.add_argument(i)
driver = webdriver.Chrome('chromedriver', options = specific_options)


# url = "https://www.acmicpc.net/"
# driver.get(url)

# login = driver.find_element(By.CLASS_NAME, "loginbar pull-right")
# login.click()

# time.sleep(1)

loginURL = "https://www.acmicpc.net/login?next=%2F"
driver.get(loginURL)

id_box = driver.find_element(By.NAME, "login_user_id")
pw_box = driver.find_element(By.NAME, "login_password")
id_box.send_keys(config.ID)
pw_box.send_keys(config.PW)

loginBtn = driver.find_element(By.ID, "submit_button")
loginBtn.click()
