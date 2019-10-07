import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(username, password, target):
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Phone number, username, or email"]')))
    driver.find_element_by_xpath('//input[@aria-label="Phone number, username, or email"]').send_keys(username)
    driver.find_element_by_xpath('//input[@aria-label="Password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(3.5)
    driver.get(f"https://www.instagram.com/{target}")
    try:
        driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
    except Exception as e:
        print(e)
    try:
        driver.find_element_by_xpath("//button[contains(text(),'Following')]")
        print(f"[{username}] SUCCESS: Now following {target}!")
    except Exception as e:
        print(f"[{username}] ERROR: An exception has occured, likely the profile is private and it has been requested.")
    time.sleep(10000)

login("username", "password", "followwhichperson")
