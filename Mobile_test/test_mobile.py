from appium import webdriver
from appium.options.android import UiAutomator2Options

import time

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "Android"
options.automation_name = "UiAutomator2"

# Replace with your actual apk name
options.app = r"C:\Users\Bhabisara Budhathoki\Desktop\QA Training\Automation\Mobile_test\app-release.apk"

driver = webdriver.Remote(
    "http://localhost:4723",
    options=options
)

driver.implicitly_wait(10)
time.sleep(5)

print("Your App Launched Successfully")

driver.quit()