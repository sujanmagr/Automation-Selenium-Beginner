#scripts to switch window or tabs
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
driver.maximize_window()
time.sleep(2)
newTab=driver.find_element(By.ID, "new-tab-button")
time.sleep(2)
newTab.click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
print("mouse is on new tab")
autocomplete=driver.find_element(*(By.XPATH,"//a[@class='btn btn-lg'][normalize-space()='Autocomplete']"))
autocomplete.click()
time.sleep(2)
driver.quit()