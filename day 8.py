"""
DAY8
----
Alerts
Frames

"""
"""
What is an Alert?

    An alert is a pop-up message box in a web page that requires user interaction to proceed.

What are the types of Alert?

    Types of alerts are: Simple Alert, Confirmation Alert, and Prompt Alert.

Write a code to perform Alert?

    alert = driver.switch_to.alert
    alert.accept()

What can we do to click OK button in alert?

    Use alert.accept() to click the OK button in an alert.

What can we do to click Cancel button in alert?

    Use alert.dismiss() to click the Cancel button in an alert.

Whether alert is an interface or class?

    Alert is an interface in Selenium.

What is mean by frames?

    Frames are HTML documents embedded within another HTML document to divide the content.

What are the arguments we pass on frames?

    Arguments for switching frames are: frame index, frame name/id, or WebElement.

Write a code for switching the alert?

    driver.switch_to.alert.accept()

Write a code to switch frames?

    driver.switch_to.frame("frameName")

What is the method to switch the alert and frame?
    
    driver.switch_to.alert for alerts and driver.switch_to.frame() for frames.

"""
"""
QUESTION 1:
----------
URL : http://demo.automationtesting.in/Alerts.html

NOTE: Click button to display an alert box and click ok button

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("http://demo.automationtesting.in/Alerts.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 2: Click the button to display the alert box
    button = driver.find_element(By.XPATH, "//button[contains(text(),'Click me')]")
    button.click()
    time.sleep(2)  # Wait for the alert to appear

    # Step 3: Switch to the alert and click OK
    alert = driver.switch_to.alert
    alert.accept()  # Click OK on the alert
    time.sleep(2)  # Wait to ensure the alert is accepted

    print("Alert accepted.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
----------
URL : http://demo.automationtesting.in/Alerts.html

NOTE: Click Alert with ok & cancel button and Click button to display an confirm box Perform confirm alert.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("http://demo.automationtesting.in/Alerts.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 2: Click the button to display the confirm box
    button = driver.find_element(By.XPATH, "//button[contains(text(),'click the button to display a confirm box')]")
    button.click()
    time.sleep(2)  # Wait for the confirm box to appear

    # Step 3: Switch to the alert and click OK
    confirm_alert = driver.switch_to.alert
    confirm_alert.accept()  # Click OK on the confirm box
    time.sleep(2)  # Wait after confirming

    print("Confirm alert accepted.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxx"""