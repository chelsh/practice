from bs4 import BeautifulSoup
import requests
import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


import config

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
specific_options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome('chromedriver', options = specific_options)

URL = config.url

driver.get(URL)
time.sleep(1)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Chelsh/Python/sugang/screenshot/first.png")

closeBtn = driver.find_element(By.NAME,'chkNoti')
closeBtn.click()
time.sleep(1)

driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Chelsh/Python/sugang/screenshot/before_login.png")

id_box = driver.find_element(By.CLASS_NAME, 'input-id')
pw_box = driver.find_element(By.CLASS_NAME, 'input-pw')
loginBtn = driver.find_element(By.CLASS_NAME, 'btn-login')

id_box.send_keys(config.stdNum)
pw_box.send_keys(config.pw)
loginBtn.click()
time.sleep(1)

driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Chelsh/Python/sugang/screenshot/after_login.png")