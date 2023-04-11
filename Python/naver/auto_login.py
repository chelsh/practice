import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import config

specific_options = webdriver.ChromeOptions()
option_list = ["--headless", "--no-sandbox", "--disable-popup-blocking"]

for op in option_list:
    specific_options.add_argument(op)

driver = webdriver.Chrome("chromedriver", options=specific_options)

naver_url = "https://www.naver.com/"

driver.get(naver_url)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Python/naver/screenshot/before.png")

naver_login = driver.find_element(By.CLASS_NAME, "link_login")
naver_login.click()

time.sleep(1)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Python/naver/screenshot/login_screen.png")

id_box = driver.find_element(By.NAME, "id")
pw_box = driver.find_element(By.NAME, "pw")
id_box.send_keys(config.ID)
pw_box.send_keys(config.PW)

login_button = driver.find_element(By.ID, "log.login")
login_button.click()

time.sleep(1)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Python/naver/screenshot/after_login!.png")