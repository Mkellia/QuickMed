from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

# Updated driver fixture with Service
@pytest.fixture(scope="module")
def driver():
    driver_path = "/path/to/chromedriver"  # Update with the path to your ChromeDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

# Test: Verify Homepage Loads
def test_homepage_load(driver):
    driver.get("http://127.0.0.1:5000")  # Replace with your app URL
    assert "QuickMed" in driver.title, "Homepage title does not match"

# Test: Signup Functionality
def test_signup(driver):
    driver.get("http://127.0.0.1:5000/signup")
    driver.find_element(By.ID, "firstname").send_keys("John")
    driver.find_element(By.ID, "lastname").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
    driver.find_element(By.ID, "number").send_keys("123456789")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.CLASS_NAME, "signup-button").click()
    assert "Welcome" in driver.page_source, "Signup failed or no welcome message"
# Test: Login Functionality
def test_login(driver):
    driver.get("http://127.0.0.1:5000/login")
    driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.CLASS_NAME, "login-button").click()
    assert "Dashboard" in driver.page_source, "Login failed or no dashboard"

# Test: Add Patient
def test_add_patient(driver):
    driver.get("http://127.0.0.1:5000/dashboard")
    driver.find_element(By.ID, "add-patient").click()
    driver.find_element(By.ID, "patient-name").send_keys("Jane Doe")
    driver.find_element(By.ID, "patient-age").send_keys("30")
    driver.find_element(By.ID, "patient-gender").send_keys("Female")
    driver.find_element(By.ID, "patient-condition").send_keys("Flu")
    driver.find_element(By.ID, "submit-patient").click()
    assert "Patient added successfully" in driver.page_source, "Add patient failed"

# Test: View Patients List
def test_view_patients(driver):
    driver.get("http://127.0.0.1:5000/patients")
    assert "Patients List" in driver.page_source, "Patients page failed to load"

# Test: Edit Patient
def test_edit_patient(driver):
    driver.get("http://127.0.0.1:5000/patients")
    driver.find_element(By.CLASS_NAME, "edit-button").click()  # Adjust selector
    driver.find_element(By.ID, "patient-condition").clear()
    driver.find_element(By.ID, "patient-condition").send_keys("Recovered")
    driver.find_element(By.ID, "update-patient").click()
  assert "Patient updated successfully" in driver.page_source, "Edit patient failed"

# Test: Delete Patient
def test_delete_patient(driver):
    driver.get("http://127.0.0.1:5000/patients")
    driver.find_element(By.CLASS_NAME, "delete-button").click()  # Adjust selector
    driver.switch_to.alert.accept()  # Confirm deletion if a confirmation dialog appears
    assert "Patient deleted successfully" in driver.page_source, "Delete patient failed"

# Test: Logout Functionality
def test_logout(driver):
    driver.get("http://127.0.0.1:5000/dashboard")
    driver.find_element(By.ID, "logout").click()
    assert "Login" in driver.page_source, "Logout failed"
