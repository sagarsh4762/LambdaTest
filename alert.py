from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_js_alert():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()

        # Handle JS Alert
        alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()
        alert = driver.switch_to.alert
        print("JS Alert Text:", alert.text)  # Print the alert text
        alert.accept()  # Accept the alert
        result = driver.find_element(By.ID, "result").text
        print("Result after JS Alert:", result)
    finally:
        time.sleep(2)
        driver.quit()

def test_js_confirm_accept():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()

        # Handle JS Confirm (Accept)
        confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        confirm_button.click()
        alert = driver.switch_to.alert
        print("JS Confirm Text:", alert.text)  # Print the confirm text
        alert.accept()  # Accept the confirm
        result = driver.find_element(By.ID, "result").text
        print("Result after accepting JS Confirm:", result)
    finally:
        time.sleep(2)
        driver.quit()

def test_js_confirm_dismiss():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()

        # Handle JS Confirm (Dismiss)
        confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        confirm_button.click()
        alert = driver.switch_to.alert
        print("JS Confirm Text:", alert.text)  # Print the confirm text
        alert.dismiss()  # Dismiss the confirm
        result = driver.find_element(By.ID, "result").text
        print("Result after dismissing JS Confirm:", result)
    finally:
        time.sleep(2)
        driver.quit()

def test_js_prompt():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.maximize_window()

        # Handle JS Prompt
        prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        prompt_button.click()
        alert = driver.switch_to.alert
        print("JS Prompt Text:", alert.text)  # Print the prompt text
        alert.send_keys("Test Input")  # Enter text into the prompt
        alert.accept()  # Accept the prompt
        result = driver.find_element(By.ID, "result").text
        print("Result after JS Prompt:", result)
    finally:
        time.sleep(2)
        driver.quit()

# Run the tests
if __name__ == "__main__":
    print("Running test for JS Alert...")
    test_js_alert()

    print("\nRunning test for JS Confirm (Accept)...")
    test_js_confirm_accept()

    print("\nRunning test for JS Confirm (Dismiss)...")
    test_js_confirm_dismiss()

    print("\nRunning test for JS Prompt...")
    test_js_prompt()