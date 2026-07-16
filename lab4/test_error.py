from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_invalid_login_error_message():
    # Connect to browser
    driver = webdriver.Chrome()

    # Get the website login url
    driver.get("https://github.com/login")

    # Input invalid github account credentials and submit
    driver.find_element(By.ID, "login_field").send_keys("username") # Invalid username
    driver.find_element(By.ID, "password").send_keys("password") # Invalid password
    driver.find_element(By.NAME, "commit").click()

    # Wait for the page to load
    time.sleep(5)

    # Verify the exact error text displays
    assert driver.find_element(By.CSS_SELECTOR, ".js-flash-alert").text.strip() == "Incorrect username or password."

    # Close the browser
    driver.quit()
