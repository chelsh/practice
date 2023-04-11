import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import config


specific_options = webdriver.ChromeOptions()
specific_options.add_argument("--headless")
specific_options.add_argument("--no-sandbox")
specific_options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome("chromedriver", options=specific_options)

URL = "https://kulms.korea.ac.kr/"
driver.get(url=URL)



close_info_xpath = "//*[@id=\"modalPush\"]/div/div/div[1]/button"
close_info = driver.find_element(By.XPATH, close_info_xpath)
close_info.click()
time.sleep(1)

blackboard_login = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/section/div/div/div/div[1]/div/div[2]/h3/strong/a")
blackboard_login.click()
time.sleep(1)

id_box = driver.find_element(By.NAME, "one_id")
pw_box = driver.find_element(By.NAME, "user_password")
id_box.send_keys(config.ID)
pw_box.send_keys(config.PW)

loginBtn = driver.find_element(By.CLASS_NAME, "userTypeCheck")
loginBtn.send_keys(Keys.ENTER)
time.sleep(1)
driver.save_screenshot("C:/Users/노채린/source/repos/workspace/Python/blackboard/screenshot/after_login.png")
