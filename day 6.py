"""
DAY6
----
Robot class
contextClick
doubleClick

"""
"""
How will you perform rightClick?

    Use the contextClick() method from the Actions class.

How will you perform doubleClick?

    Use the doubleClick() method from the Actions class.

Write a code for Robot class?

    Robot robot = new Robot();

In which package is the Robot class available?

    The Robot class is available in the java.awt package.

What exception does the Robot class throw?

    The Robot class throws the AWTException.

What is the method to perform rightClick?

    The method is contextClick() in the Actions class.

What is the method to perform doubleClick?

    The method is doubleClick() in the Actions class.

Write a code to copy a text using the Robot class?

    Robot robot = new Robot();
    robot.keyPress(KeyEvent.VK_CONTROL);
    robot.keyPress(KeyEvent.VK_C);
    robot.keyRelease(KeyEvent.VK_C);
    robot.keyRelease(KeyEvent.VK_CONTROL);

Write a code to paste a text using the Robot class?

    Robot robot = new Robot();
    robot.keyPress(KeyEvent.VK_CONTROL);
    robot.keyPress(KeyEvent.VK_V);
    robot.keyRelease(KeyEvent.VK_V);
    robot.keyRelease(KeyEvent.VK_CONTROL);

In which class is contextClick() available?

    The contextClick() method is available in the Actions class.

In which class is doubleClick() available?

    The doubleClick() method is available in the Actions class.

"""
"""
QUESTION 1
----------
URL : https://www.facebook.com/

NOTE: Type email in email textbox and cut  the email using Robot class 
      Paste that email in password text  using Robot class 

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
driver.maximize_window()

# Navigate to Facebook
driver.get("https://www.facebook.com/")

# Locate the email textbox and type an email
email_textbox = driver.find_element(By.ID, "email")
email_textbox.send_keys("testemail@example.com")

# Wait for the input to be typed
time.sleep(2)

# Cut the email using pyautogui (Robot-like functionality)
email_textbox.click()  # Click on the email textbox to focus
time.sleep(1)

# Select all text (CTRL + A)
pyautogui.hotkey("ctrl", "a")
time.sleep(1)

# Cut the text (CTRL + X)
pyautogui.hotkey("ctrl", "x")
time.sleep(1)

# Locate the password textbox and paste the email
password_textbox = driver.find_element(By.ID, "pass")
password_textbox.click()  # Focus on the password textbox
time.sleep(1)

# Paste the text (CTRL + V)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# Close the browser
driver.quit()


