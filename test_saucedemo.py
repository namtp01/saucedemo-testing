import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# A PyTest Fixture is a setup/teardown function.
# This 'driver' fixture will run before each test function.
# It sets up the Chrome browser and yields it to the test.
# After the test finishes, it will run the 'driver.quit()' part.
@pytest.fixture
def driver():
    # Setup: Initialize a new Chrome browser instance
    driver = webdriver.Chrome()
    
    # We add an implicit wait. This tells Selenium to wait
    # up to 10 seconds for an element to appear if it's not
    # immediately available. This makes our tests more stable.
    driver.implicitly_wait(10)
    
    # 'yield' passes the driver object to the test function.
    yield driver
    
    # Teardown: This code runs after the test is complete.
    # We add a short pause so you can see the final state.
    time.sleep(2)
    driver.quit()

# --- TEST CASES START HERE ---
# PyTest finds any function that starts with 'test_'

def test_successful_login(driver):
    """
    Automates Test Case TC-001: Login with valid credentials.
    """
    # Step 1: Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    
    # Step 2: Enter username
    # We find the element by its 'ID' and send keys to it.
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # Step 3: Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Step 4: Click Login button
    driver.find_element(By.ID, "login-button").click()
    
    # Verification (Assertion)
    # We check that the current URL is the inventory page.
    # If this is False, PyTest will mark the test as FAILED.
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == expected_url, "Login failed or did not redirect to inventory page."

def test_invalid_password(driver):
    """
    Automates Test Case TC-002: Login with an invalid password.
    """
    # Step 1: Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Step 2: Enter valid username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Step 3: Enter password
    driver.find_element(By.ID, "password").send_keys("wrong_password")

    # Step 4: Click login button
    driver.find_element(By.ID, "login-button").click()

    # Verification (Assertion)
    # We find the error message element (it's an h3 tag).
    # We use a CSS_SELECTOR to find it by its 'data-test' attribute.
    error_message_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

    # Get the actual text from the element.
    actual_message = error_message_element.text

    # Verification (Assertion)
    # We check that the current URL is the inventory page.
    # If this is False, PyTest will mark the test as FAILED.
    expected_message = "Epic sadface: Username and password do not match any user in this service"
    assert actual_message == expected_message, f"Incorrect error message. Expected: '{expected_message}', Got: '{actual_message}'"

def test_locked_out_user(driver):
    """
    Automates Test Case TC-003: Login with a locked-out user.
    """
    # Step 1: Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    
    # Step 2: Enter locked-out username
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    
    # Step 3: Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Step 4: Click Login button
    driver.find_element(By.ID, "login-button").click()
    
    # Verification (Assertion)
    # We find the error message element (it's an h3 tag).
    # We use a CSS_SELECTOR to find it by its 'data-test' attribute.
    error_message_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    
    # Get the actual text from the element.
    actual_message = error_message_element.text
    
    # Check if the text is what we expect.
    expected_message = "Epic sadface: Sorry, this user has been locked out."
    assert actual_message == expected_message, f"Incorrect error message. Expected: '{expected_message}', Got: '{actual_message}'"