from selenium.webdriver.common.by import By

# Test: Schedule Appointment
def test_schedule_appointment(driver):
    driver.get("http://127.0.0.1:5000/appointments")
    driver.find_element(By.ID, "patient-id").send_keys("1")  # Use a valid patient ID
    driver.find_element(By.ID, "date").send_keys("2024-12-01")
    driver.find_element(By.ID, "time").send_keys("10:00 AM")
    driver.find_element(By.CLASS_NAME, "schedule-button").click()
    assert "Appointment scheduled successfully" in driver.page_source, "Schedule appointment failed"

# Test: View Appointments
def test_view_appointments(driver):
    driver.get("http://127.0.0.1:5000/view-appointments")
    assert "Scheduled Appointments" in driver.page_source, "View appointments page failed to load"

# Test: Cancel Appointment
def test_cancel_appointment(driver):
    driver.get("http://127.0.0.1:5000/view-appointments")
    driver.find_element(By.CLASS_NAME, "cancel-appointment-button").click()  # Adjust selector
    driver.switch_to.alert.accept()  # Confirm cancellation
    assert "Appointment cancelled successfully" in driver.page_source, "Cancel appointment failed"

