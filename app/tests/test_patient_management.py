from selenium.webdriver.common.by import By

# Test: Register Patient
def test_register_patient(driver):
    driver.get("http://127.0.0.1:5000/register-patient")
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "dob").send_keys("1990-01-01")
    driver.find_element(By.ID, "contact").send_keys("123456789")
    driver.find_element(By.ID, "medical-history").send_keys("None")
    driver.find_element(By.CLASS_NAME, "register-button").click()
    assert "Patient registered successfully" in driver.page_source, "Register patient failed"

# Test: View Patient List
def test_view_patient_list(driver):
    driver.get("http://127.0.0.1:5000/patient-list")
    assert "Patient List" in driver.page_source, "View patient list failed"

~     
