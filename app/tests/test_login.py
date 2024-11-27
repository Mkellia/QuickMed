from selenium.webdriver.common.by import By

# Test: Login with Valid Credentials
def test_login_valid_credentials(driver):
    driver.get("http://127.0.0.1:5000/login")
    driver.find_element(By.ID, "email").send_keys("alice.johnson@example.com")
    driver.find_element(By.ID, "password").send_keys("securepassword123")
    driver.find_element(By.CLASS_NAME, "login-button").click()
    assert "Dashboard" in driver.page_source, "Login with valid credentials failed"
