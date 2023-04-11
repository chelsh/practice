from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime

import config

URL = "https://people.mcd.co.kr/main/login.do"

specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)

driver.get(url=URL)

company_code = driver.find_element(By.NAME, "txtComp")
company_code.send_keys(config.COMPANY_CODE)

user_id = driver.find_element(By.NAME, "txtId")
user_id.send_keys(config.USER_ID)

password = driver.find_element(By.NAME, "txtPwd")
password.send_keys(config.PASSWORD)

loginBtn = driver.find_element(By.CLASS_NAME, "loginBtn")
loginBtn.click()
time.sleep(1)

dob_box = driver.find_element(By.ID, "SSN1")
dob_box.send_keys(config.DOB)

submitBTn = driver.find_element(By.ID, "btnAppr")
submitBTn.click()
time.sleep(1)



manageSKDL = driver.find_element(By.XPATH, "//*[@id=\"top_menu_id\"]/li[2]/a")
manageSKDL.click()
time.sleep(1)
driver.save_screenshot(config.screenshot_loc_header + "after_click_mngSKDL.png")

def applySKDL():
    TODAY = datetime.datetime.strptime
    YEAR = TODAY.year
    MONTH = TODAY.month
    DATE = TODAY.date
    
    print(f"Start applying schedule of ")





def confirmSKDL():
    pass

def main():
    print()
