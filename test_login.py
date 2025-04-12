from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import pytest

from pathlib import Path

# Explicitly load the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, override=True)

# Credentials
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

@pytest.fixture(scope="function")
def setup_browser():
    driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
    driver.implicitly_wait(10)
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_valid_login(setup_browser: WebDriver):
    driver = setup_browser
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
    assert "You logged into a secure area!" in success_message

def test_invalid_login(setup_browser: WebDriver):
    driver = setup_browser
    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("invalid_pass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".flash.error").text
    assert "Your username is invalid!" in error_message