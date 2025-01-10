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

"""

"""
QUESTION 2
-----------
URL:  http://www.amazon.in

NOTE: Try Prime first mouseover
      Click Free fast delievery on prime items

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

try:
    # Open Amazon India
    driver.get("http://www.amazon.in")
    driver.maximize_window()
    
    # Locate the "Try Prime" menu using its XPath or CSS selector
    try_prime_element = driver.find_element(By.XPATH, "//span[contains(text(), 'Try Prime')]")
    
    # Perform mouseover using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(try_prime_element).perform()
    
    # Allow time for the dropdown to appear
    time.sleep(2)
    
    # Locate and click "Free fast delivery on Prime items"
    free_delivery_element = driver.find_element(By.LINK_TEXT, "Free fast delivery on Prime items")
    free_delivery_element.click()
    
    # Wait for a while to observe the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 3
----------
URL : http://www.flipkart.com

NOTE: Home & Furniture is first mouseover 
      Click Bath Towels and print any product name 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

try:
    # Open Flipkart
    driver.get("http://www.flipkart.com")
    driver.maximize_window()

    # Close the login popup (pressing the Escape key or clicking the close button)
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
        close_popup.click()
    except Exception as e:
        print("No popup to close:", e)

    # Locate the "Home & Furniture" menu
    home_furniture = driver.find_element(By.XPATH, "//span[text()='Home & Furniture']")

    # Perform mouseover using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(home_furniture).perform()

    # Allow time for the dropdown to appear
    time.sleep(2)

    # Locate and click "Bath Towels"
    bath_towels = driver.find_element(By.LINK_TEXT, "Bath Towels")
    bath_towels.click()

    # Wait for the page to load
    time.sleep(5)

    # Find and print the name of any product
    product_name = driver.find_element(By.XPATH, "//a[contains(@class, 'IRpwTa')]").text
    print("Product Name:", product_name)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 4
----------
URL : https://www.shopclues.com/wholesale.html
 
NOTE: Mobile and electronics is first mouseover 
      Click Smart Phones range Rs5001 - Rs10000

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open ShopClues
    driver.get("https://www.shopclues.com/wholesale.html")
    driver.maximize_window()

    # Locate the "Mobiles & Electronics" menu
    mobiles_electronics = driver.find_element(By.XPATH, "//a[text()='Mobiles & Electronics']")

    # Perform mouseover using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(mobiles_electronics).perform()

    # Allow time for the dropdown to appear
    time.sleep(2)

    # Locate and click "Smart Phones range Rs5001 - Rs10000"
    smartphones_range = driver.find_element(By.XPATH, "//a[text()='Smart Phones range Rs5001 - Rs10000']")
    smartphones_range.click()

    # Wait for the page to load
    time.sleep(5)

    # Print the page title to confirm navigation
    print("Page Title:", driver.title)

finally:
    # Close the browser
    driver.quit()

xxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 5
----------
URL : https://www.shopclues.com/wholesale.html 
 
NOTE: Sports&more  is first mouseover
      Click weights grainers

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open ShopClues
    driver.get("https://www.shopclues.com/wholesale.html")
    driver.maximize_window()

    # Locate the "Sports & More" menu
    sports_more = driver.find_element(By.XPATH, "//a[text()='Sports & More']")

    # Perform mouseover using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(sports_more).perform()

    # Allow time for the dropdown to appear
    time.sleep(2)

    # Locate and click "Weights Grainers"
    weights_trainers = driver.find_element(By.XPATH, "//a[text()='Weights Grainers']")
    weights_trainers.click()

    # Wait for the page to load
    time.sleep(5)

    # Print the page title to confirm navigation
    print("Page Title:", driver.title)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxx"""

"""

"""

