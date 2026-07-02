from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_user_login():
    # Connect to browser
    driver = webdriver.Chrome()

    # Get the website login url
    driver.get("https://github.com/login")

    # Input github account credentials and submit
    driver.find_element(By.ID, "login_field").send_keys("") # Enter your username
    driver.find_element(By.ID, "password").send_keys("") # Enter your password
    driver.find_element(By.NAME, "commit").click()

    # Wait for the page to load
    time.sleep(5)

    # Verify whether the login was successful
    # Change == to != to verify unsuccessful login
    assert driver.current_url == "https://github.com/" or "https://github.com/sessions/verified-device" 

    # Close the browser
    driver.quit()