from selenium.webdriver.common.by import By

# Test: Logout Functionality
def test_logout(driver):
    driver.get("http://127.0.0.1:5000/dashboard")
    driver.find_element(By.ID, "logout").click()
    assert "Login" in driver.page_source, "Logout failed"

