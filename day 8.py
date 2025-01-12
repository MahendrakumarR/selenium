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

"""
QUESTION 3
----------
URL : http://demo.automationtesting.in/Alerts.html

NOTE: Click Alert with textBox button and Click button to demonstrate an prompt box Perform prompt alert.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("http://demo.automationtesting.in/Alerts.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 2: Click the "Alert with Textbox" tab
    text_box_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Alert with Textbox')]")
    text_box_tab.click()
    time.sleep(2)  # Wait for the tab to load

    # Step 3: Click the "Click me" button to display the prompt box
    button = driver.find_element(By.XPATH, "//button[contains(text(),'click the button to demonstrate the prompt box')]")
    button.click()
    time.sleep(2)  # Wait for the prompt box to appear

    # Step 4: Switch to the alert, enter text, and click OK
    prompt_alert = driver.switch_to.alert
    prompt_alert.send_keys("Selenium Automation")  # Enter text into the prompt box
    time.sleep(1)  # Wait to ensure the text is entered
    prompt_alert.accept()  # Click OK on the prompt box
    time.sleep(2)  # Wait after accepting the prompt

    print("Prompt alert handled successfully.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 4
----------
URL : https://netbanking.hdfcbank.com/netbanking/?_ga=2.176378149.1819882415.1533883212-608727520.1532670997

NOTE: Click continue without enter the user id and handle popup.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the HDFC NetBanking URL
    driver.get("https://netbanking.hdfcbank.com/netbanking/?_ga=2.176378149.1819882415.1533883212-608727520.1532670997")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Switch to the login frame
    driver.switch_to.frame("login_page")  # Switch to the iframe containing the login form

    # Step 3: Click the "Continue" button without entering the user ID
    continue_button = driver.find_element(By.XPATH, "//a[@onclick='return fLogon();']")
    continue_button.click()
    time.sleep(2)  # Wait for the alert to appear

    # Step 4: Handle the alert popup
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)  # Print the alert text for verification
    alert.accept()  # Click OK to dismiss the alert
    time.sleep(2)  # Wait after handling the alert

    print("Alert handled successfully.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 5
----------
URL : https://netbanking.canarabank.in/entry/ENULogin.jsp

NOTE: Click sign in without enter the user id and print text appear and handle popup.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Canara Bank NetBanking URL
    driver.get("https://netbanking.canarabank.in/entry/ENULogin.jsp")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Click the "Sign In" button without entering the user ID
    sign_in_button = driver.find_element(By.XPATH, "//input[@value='SIGN IN']")
    sign_in_button.click()
    time.sleep(2)  # Wait for the alert to appear

    # Step 3: Handle the popup alert
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)  # Print the alert text for verification
    alert.accept()  # Click OK to dismiss the alert
    time.sleep(2)  # Wait after handling the alert

    print("Popup handled successfully.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 6
----------
URL : https://retail.onlinesbi.com/retail/login.htm

NOTE: Click Continue To Login and click Login without enter the user id.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the SBI NetBanking URL
    driver.get("https://retail.onlinesbi.com/retail/login.htm")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Click "Continue to Login"
    continue_to_login_button = driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE TO LOGIN')]")
    continue_to_login_button.click()
    time.sleep(3)  # Wait for the login page to load

    # Step 3: Click the "Login" button without entering the user ID
    login_button = driver.find_element(By.ID, "Button2")
    login_button.click()
    time.sleep(2)  # Wait for the alert to appear

    # Step 4: Handle the popup alert
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)  # Print the alert message
    alert.accept()  # Click OK to dismiss the alert
    time.sleep(2)  # Wait after handling the alert

    print("Alert handled successfully.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 7
----------
URL : https://netbanking.hdfcbank.com/netbanking/

NOTE: Enter the userId,click continue.Enter password.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the HDFC NetBanking URL
    driver.get("https://netbanking.hdfcbank.com/netbanking/")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Switch to the login frame
    driver.switch_to.frame("login_page")  # Switch to the iframe containing the login form

    # Step 3: Enter the User ID
    user_id_field = driver.find_element(By.NAME, "fldLoginUserId")
    user_id_field.send_keys("YourUserID")  # Replace 'YourUserID' with the actual User ID
    time.sleep(1)  # Wait after entering the User ID

    # Step 4: Click the "Continue" button
    continue_button = driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE')]")
    continue_button.click()
    time.sleep(3)  # Wait for the password field to appear

    # Step 5: Enter the Password
    password_field = driver.find_element(By.NAME, "fldPassword")
    password_field.send_keys("YourPassword")  # Replace 'YourPassword' with the actual password
    time.sleep(1)  # Wait after entering the password

    print("User ID and password entered successfully.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 8
----------
URL : https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI

NOTE: Enter the userId password.
      Click login button

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the ICICI Bank NetBanking URL
    driver.get("https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Enter the User ID
    user_id_field = driver.find_element(By.NAME, "AuthenticationFG.USER_PRINCIPAL")
    user_id_field.send_keys("YourUserID")  # Replace 'YourUserID' with the actual User ID
    time.sleep(1)  # Wait after entering the User ID

    # Step 3: Enter the Password
    password_field = driver.find_element(By.NAME, "AuthenticationFG.ACCESS_CODE")
    password_field.send_keys("YourPassword")  # Replace 'YourPassword' with the actual password
    time.sleep(1)  # Wait after entering the password

    # Step 4: Click the "Login" button
    login_button = driver.find_element(By.ID, "VALIDATE_CREDENTIALS1")
    login_button.click()
    time.sleep(3)  # Wait after clicking the login button

    print("Login process executed successfully.")

finally:
    # Close the browser
    driver.quit()
"""