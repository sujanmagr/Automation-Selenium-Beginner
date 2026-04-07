from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/dropdown")


# dropdown=driver.find_element(By.ID, "dropdownMenuButton")

# dropdown.click()


dropdown=Select(driver.find_element(By.ID, "dropdownMenuButton"))

try:
    dropdown.Select_by_visible_text("modal")
    print("selected modal")
except:
    print("modal not selected")
# dropdown1=driver.find_element(By.ID, "dropdownMenuButton")
# dropdown1.click()
# time.sleep(2)
# option_click=driver.find_element(By.XPATH, "/html/body/div/div/div/a[5]")
# option_click.click()

time.sleep(2)
driver.quit()

