"""
DAY 6
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
driver = webdriver.Firefox()  # Ensure ChromeDriver is in your PATH
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
----------
URL : https://www.google.co.in/webhp 

NOTE: Enter Vel Murugan and select Vel Murugan using double Click
      Cut Vel Murugan using Keyboard shortcut[Ctrl+x]

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Firefox()

try:
    # Open Google homepage
    driver.get("https://www.google.co.in/webhp")
    driver.maximize_window()

    # Locate the search bar
    search_box = driver.find_element(By.NAME, "q")

    # Enter "Vel Murugan" in the search bar
    search_box.send_keys("Vel Murugan")
    time.sleep(1)

    # Select "Vel Murugan" using double-click
    actions = ActionChains(driver)
    actions.double_click(search_box).perform()
    time.sleep(1)

    # Cut the text using Ctrl+X
    search_box.send_keys(Keys.CONTROL, "x")
    time.sleep(1)

    # Confirm the search bar is empty
    print("Search bar text after cut:", search_box.get_attribute("value"))

finally:
    # Close the browser
    driver.quit()
"""
"""
QUESTION 3
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click interview question and Right click cts interview question and Select open link in new window

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Firefox()

try:
    # Open the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()

    # Locate and click "Interview Question"
    interview_question = driver.find_element(By.XPATH, "Interview Question")
    interview_question.click()
    time.sleep(2)

    # Locate the "CTS Interview Question" link
    cts_interview_question = driver.find_element(By.LINK_TEXT, "CTS Interview Question")

    # Right-click on the "CTS Interview Question" link
    actions = ActionChains(driver)
    actions.context_click(cts_interview_question).perform()

    # Open link in a new window using keyboard shortcut
    actions.send_keys(Keys.CONTROL + Keys.RETURN).perform()
 
    # Wait to see the action in the new window
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx """

"""
QUESTION 4
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Right Click Framework Test Papers  and Select Inspect

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
 
# Set up the WebDriver
driver = webdriver.Firefox()

try:
    # Open the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()
 
    # Locate the "Framework Test Papers" link
    framework_test_papers = driver.find_element(By.ID, "heading304")

    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", framework_test_papers)
    
    # Right-click on the "Framework Test Papers" link
    actions = ActionChains(driver)
    actions.context_click(framework_test_papers).perform()

    

    # Wait for some time to observe the action
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
"""

"""
QUESTION 5
-----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click Model Resume and  rightClick resume model 4 the page and click save as.
"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import requests

# Set up the driver
driver = webdriver.Firefox()  # or use Edge/Firefox based on your setup
driver.get("http://greenstech.in/selenium-course-content.html")
driver.maximize_window()

time.sleep(3)  # Allow page to load

# Click the "Model Resume" link to open the modal
model_resume_button = driver.find_element(By.XPATH, "//h2[contains(text(),'Model Resume')]")
model_resume_button.click()
time.sleep(2)

# Locate "Resume Model 4"
resume_model_4 = driver.find_element(By.XPATH, "//a[contains(text(),'Resume Model-4')]")

# Get the href attribute of the link (the file URL)
file_url = resume_model_4.get_attribute("href")
print("Resume 4 download link:", file_url)

# Download the file directly using requests
response = requests.get(file_url)
filename = file_url.split("/")[-1]

with open(filename, "wb") as file:
    file.write(response.content)

print(f"Downloaded '{filename}' successfully.")

# Clean up
driver.quit()

"""

"""
QUESTION 6
-----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Right Click RPA [ below Top Selenium Trends In 2020] and click Inspect

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Firefox()

try:
    # Open the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()

    # Locate the "RPA" link below "Top Selenium Trends In 2020"
    rpa_link = driver.find_element(By.XPATH, "//h2[text()='Top Selenium Trends In 2020']/following::a[text()='RPA']")

    # Right-click (context-click) on the "RPA" link
    actions = ActionChains(driver)
    actions.context_click(rpa_link).perform()

    # Wait for some time to observe the right-click action
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()


"""
QUESTION 7
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click Selenium Test Papaers Right Click Day 6 Robot and select Inspect

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()

    # Locate and click on "Selenium Test Papers"
    selenium_test_papers_link = driver.find_element(By.LINK_TEXT, "Selenium Test Papers")
    selenium_test_papers_link.click()
    time.sleep(2)  # Wait for the page to load if necessary

    # Locate the "Day 6 Robot" link
    day_6_robot_link = driver.find_element(By.LINK_TEXT, "Day 6 Robot")

    # Right-click (context-click) on the "Day 6 Robot" link
    actions = ActionChains(driver)
    actions.context_click(day_6_robot_link).perform()

    # Wait for some time to observe the right-click action
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxx"""

"""

Question 8
----------
URL : https://www.flipkart.com/

NOTE: Click login
      Type a  name in email textbox and cut using (control +c) and paste in password using (control+v)

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open Flipkart login page
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    # Wait for page to load and close the pop-up
    time.sleep(3)
    close_button = driver.find_element(By.XPATH, "//button[text()='✕']")
    close_button.click()

    # Click on the Login button
    login_button = driver.find_element(By.XPATH, "//a[@href='/account/login']")
    login_button.click()
    time.sleep(2)  # Wait for the login page to load

    # Locate the email text box and type a name
    email_textbox = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    email_textbox.send_keys("TestName")

    # Cut the text using Ctrl+C (simulating cut)
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    time.sleep(1)

    # Locate the password text box and paste the text using Ctrl+V (simulating paste)
    password_textbox = driver.find_element(By.XPATH, "//input[@type='password']")
    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    # Wait to observe the actions
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 9
------------
URL : https://www.amazon.in/

NOTE: Click login and type a  email in email textbox and select email and right click and click cut 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open the Amazon URL
    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(3)

    # Click on the Login button
    login_button = driver.find_element(By.XPATH, "//span[text()='Hello, Sign in']")
    login_button.click()
    time.sleep(2)  # Wait for the login page to load

    # Locate the email textbox and type an email
    email_textbox = driver.find_element(By.ID, "ap_email")
    email_textbox.send_keys("testemail@example.com")
    time.sleep(1)

    # Select the email text (simulating the "Ctrl + A" shortcut)
    actions = ActionChains(driver)
    actions.move_to_element(email_textbox).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(1)

    # Right-click (context-click) and simulate 'Cut' using "Ctrl + X"
    actions.context_click(email_textbox).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()

    # Wait to observe the actions
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()

xxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 10
-----------
URL : https://www.snapdeal.com/offers/quirky

NOTE: Select any item and then right click and press open in a new window

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open the Snapdeal quirky offers page
    driver.get("https://www.snapdeal.com/offers/quirky")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(3)

    # Select an item (just selecting the first item in the list as an example)
    first_item = driver.find_element(By.XPATH, "//div[@class='product-tuple-image ']//a")
    first_item.click()

    # Wait for the product page to load (optional)
    time.sleep(2)

    # Simulate opening the link in a new window (Ctrl + Click)
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(first_item).key_up(Keys.CONTROL).perform()

    # Wait to observe the actions
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 11
-----------
URL : https://www.flipkart.com/

NOTE: Select any item and then right click and press Save link as

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Open Flipkart URL
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    # Wait for the page to load and close any pop-up
    time.sleep(3)
    close_button = driver.find_element(By.XPATH, "//button[text()='✕']")
    close_button.click()

    # Select the first product link on the page (you can modify the XPath to select any product)
    product_link = driver.find_element(By.XPATH, "//a[@class='_1fQZEK']")
    
    # Get the product URL
    product_url = product_link.get_attribute("href")

    # Use the requests library to download the product URL (or save it as required)
    # Example: Let's download the image associated with the product
    print(f"Downloading the content from: {product_url}")
    response = requests.get(product_url)

    # Save the content to a file (you can modify the filename or content as needed)
    with open("product_page.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    print("File saved successfully!")

finally:
    # Close the browser
    driver.quit()
"""





