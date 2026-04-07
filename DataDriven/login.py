import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN_URL = "https://www.saucedemo.com/"   

USERNAME_LOCATOR = (By.ID, "user-name")   
PASSWORD_LOCATOR = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")

driver=webdriver.Chrome()
driver.maximize_window()

def login_test(username, password):
    driver.get(LOGIN_URL)
    time.sleep(2)

    # Enter username
    driver.find_element(*USERNAME_LOCATOR).clear()
    driver.find_element(*USERNAME_LOCATOR).send_keys(username)

    # Enter password
    driver.find_element(*PASSWORD_LOCATOR).clear()
    driver.find_element(*PASSWORD_LOCATOR).send_keys(password)

    # Click login
    driver.find_element(*LOGIN_BUTTON).click()
    time.sleep(3)

    # Validate login
    if "inventory" in driver.current_url:
        print(f"Login successful for user: {username}")
    else:
        print(f"Login unsuccessful for user: {username}")

# Read CSV file
with open("login_data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row["username"]
        password = row["password"]
        login_test(username, password)

driver.quit()
