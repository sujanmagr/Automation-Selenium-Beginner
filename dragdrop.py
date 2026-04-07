#script to drag and drop a file 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
# storing url to a variable
url="https://formy-project.herokuapp.com/dragdrop"
driver.get(url)
#maximize window
driver.maximize_window()
time.sleep(3)
drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='image']//img")))
drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='box']")))
wait=ActionChains(driver)
wait.drag_and_drop(drag, drop).perform()
#quit window after 3 sec
time.sleep(3)
driver.quit()

 