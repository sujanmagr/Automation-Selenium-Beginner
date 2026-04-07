import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
url="https://www.saucedemo.com/"
driver.get(url)
actions=ActionChains(driver)
login_button=driver.find_element(By.ID,"login-button")
actions.context_click(login_button).perform()
time.sleep(3)
driver.quit()
