from selenium.webdriver.common.by import By

# Test: Add Staff
def test_add_staff(driver):
    driver.get("http://127.0.0.1:5000/staff-management")
    driver.find_element(By.ID, "staff-name").send_keys("Alice Johnson")
    driver.find_element(By.ID, "role").send_keys("Nurse")
    driver.find_element(By.CLASS_NAME, "add-staff-button").click()
    assert "Staff member added successfully" in driver.page_source, "Add staff failed"

# Test: View Staff
def test_view_staff(driver):
    driver.get("http://127.0.0.1:5000/view-staff")
    assert "Registered Staff" in driver.page_source, "View staff page failed to load"

# Test: Edit Staff
def test_edit_staff(driver):
    driver.get("http://127.0.0.1:5000/view-staff")
    driver.find_element(By.CLASS_NAME, "edit-staff-button").click()  # Adjust selector
    driver.find_element(By.ID, "role").clear()
    driver.find_element(By.ID, "role").send_keys("Senior Nurse")
    driver.find_element(By.CLASS_NAME, "save-staff-button").click()
    assert "Staff updated successfully" in driver.page_source, "Edit staff failed"

# Test: Delete Staff
def test_delete_staff(driver):
    driver.get("http://127.0.0.1:5000/view-staff")
    driver.find_element(By.CLASS_NAME, "delete-staff-button").click()  # Adjust selector
    driver.switch_to.alert.accept()  # Confirm deletion
    assert "Staff deleted successfully" in driver.page_source, "Delete staff failed"

