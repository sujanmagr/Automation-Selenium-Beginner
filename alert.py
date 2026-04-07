from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.maximize_window()
url="https://demoqa.com/alerts"
driver.get(url)
time.sleep(2)

alert_button=driver.find_element(By.ID, "promtButton")
alert_button.click()
wait=WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())
# time.sleep(1)
# driver.switch_to.alert.send_keys('sachin')
alert=driver.switch_to.alert
time.sleep(2)
alert.send_keys("Hello this is alert textbox")

time.sleep(2)
driver.quit()
