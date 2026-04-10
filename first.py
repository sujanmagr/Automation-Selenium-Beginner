# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.support.ui import Select

# driver=webdriver.Chrome()
# wait=WebDriverWait(driver, 10)
# driver.maximize_window()
# url="https://www.saucedemo.com/"
# driver.get(url)
# time.sleep(2)
# username=driver.find_element(By.XPATH, "//input[@name = 'user-name']")
# username.send_keys("standard_user")
# password=driver.find_element(By.XPATH,"//input[@id='password']")
# password.send_keys("secret_sauce")
# login_button=driver.find_element(By.ID, "login-button")
# login_button.click()
# try:
#     print("Hello this is try block")
#     login_button.click()

# except:
#     print("This is except block")
#     print("The button is not clicked")
# time.sleep(3)



# dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
# dropdown.select_by_visible_text("Price (low to high)")
# time.sleep(3)
#assertion url
# assert "Product" in driver.current_url, "Failed: Login failed/Unsuccessful"
# driver.execute_script("window.scrollBy(0,400);")
# time.sleep(3)
# final_element=driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
# final_element.click()
# driver.quit()


# url="https://www.saucedemo.com/"

# driver.get(url)

# username=driver.find_element(By.ID, "user-name").send_keys("standard_user")
# password=driver.find_element(By.ID, "password").send_keys("password")


# login_button=driver.find_element(By.ID, "Login-button").click()
# time.sleep(3)
# driver.quit()





# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# driver=webdriver.Chrome()
# driver.maximize_window()

# url="https://www.saucedemo.com/"
# driver.get(url)

# username=driver.find_element(By.XPATH,"//input[@id='user-name']")
# username.send_keys("standard_user")
# time.sleep(1)

# password=driver.find_element(By.ID, "password")
# password.send_keys("secret_sauce")
# time.sleep(1)

# # wait=WebDriverWait(driver,10)

# login_button=driver.find_element(By.ID,"login-button")
# login_button.click()


# # driver.execute_script("window.scrollBy(0,400)")



# # 1. URL Validation
# # assert "inventory" in driver.current_url, "Failed: Not on the dashboard page"

# # if "Swag Labs" in driver.title:
# #     print("login succcessful")

# # else:
# #     print("login unsuccessful")

# time.sleep(3)
# driver.quit()



# from file import myclass
# myobj=myclass()
# myobj.printag()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
url="https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)
username=driver.find_element(By.XPATH, "//*[@id='user-name']")
username.send_keys("standard_user")
password=driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauce")
login_button=driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)
driver.quit()












