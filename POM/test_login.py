from selenium import webdriver
import time
from page.login import loginpage
import pytest
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    login_page=loginpage(driver)
    login_page.open_page("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(3)
    login_page.enter_username("standard_user")
    time.sleep(1)

    login_page.enter_password("secret_sauce")
    time.sleep(1)

    login_page.click_login()
    time.sleep(4)

    assert "product" in driver.current_url
   





# pip install pytest selenium
#pytest -k test_login
