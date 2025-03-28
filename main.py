from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=4195337096&f_AL=true&geoId=103644278&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true'
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get(LINKEDIN_URL)

sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

time.sleep(2)
email_field = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
password_field.send_keys(PASSWORD)
next_sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
next_sign_in_button.click()

time.sleep(15)

# TODO - Find elements value needs to be altered to access job elements
jobs = driver.find_elements(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li')
# jobs = driver.find_elements(By.CSS_SELECTOR, 'a span strong')

for job in jobs:
    try:
        time.sleep(2)
        job.click()
    except NoSuchElementException:
        continue
# driver.quit()