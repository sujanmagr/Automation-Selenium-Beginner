from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
# Open website
driver.get("https://demoqa.com/alerts")

wait = WebDriverWait(driver, 10)

# Override prompt to return value automatically
driver.execute_script("window.prompt = function(){ return 'Sachin'; }")

# Click the prompt button
driver.find_element(By.ID, "promtButton").click()

# Wait for result to appear on page
result = wait.until(
    EC.visibility_of_element_located((By.ID, "promptResult"))
)
# Print result
print(result.text)
# Optional validation
assert "Sachin" in result.text

# Close browser
driver.quit()


from selenium.webdriver.support.ui import Select
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Nepal")