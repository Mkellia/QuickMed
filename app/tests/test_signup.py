from selenium.webdriver.common.by import By

# Test: Signup with Valid Details
def test_signup_valid_details(driver):
    driver.get("http://127.0.0.1:5000/signup")
    driver.find_element(By.ID, "firstname").send_keys("Alice")
    driver.find_element(By.ID, "lastname").send_keys("Johnson")
    driver.find_element(By.ID, "email").send_keys("alice.johnson@example.com")
    driver.find_element(By.ID, "number").send_keys("987654321")
    driver.find_element(By.ID, "password").send_keys("securepassword123")
    driver.find_element(By.CLASS_NAME, "signup-button").click()
    assert "Welcome" in driver.page_source, "Signup with valid details failed"

