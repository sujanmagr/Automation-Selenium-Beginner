from selenium import webdriver
import pytest
from pages.login import loginpage
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
#parametrize decorator 
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),#valid user
    ("sachin", "sauce")#invalid user
])
def test_login(driver, username, password):
    login = loginpage(driver)
    login.open_url("https://www.saucedemo.com/")
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    time.sleep(2)
    assert "inventory" in driver.current_url
def test_home(driver):
    pass
    


