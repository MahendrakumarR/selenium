"""
DAY7
----
Screenshot
scrollup and scrolldown

"""
"""
How will you take a screenshot in Selenium?

    Use the get_screenshot_as_file() method in Python or TakesScreenshot interface in Java.

For what reason do we take screenshots?

    To capture the current state of the web page for debugging, reporting, or validation purposes.

Whether TakesScreenshot is a class or interface?

    TakesScreenshot is an interface.

In what place will the screenshot store by default?

    By default, the screenshot is stored in the specified path when saved using code.

Write a code to perform a screenshot?

    Python: driver.save_screenshot('screenshot.png').

Whether FileUtils is a class or interface?

    FileUtils is a class in Java (part of Apache Commons IO library).

Suppose we want to change the location of the screenshot. What can we do?

    Specify a custom file path when saving the screenshot.

What is JavaScript?

    JavaScript is a programming language used to make web pages interactive.

Write a code for scroll up and scroll down?

    Python:

    driver.execute_script("window.scrollBy(0, 500);")  # Scroll down
    driver.execute_script("window.scrollBy(0, -500);")  # Scroll up

In which method do scroll up and scroll down take place?

    In the execute_script() method.

Whether JavaScript is a class or interface?

    JavaScript is neither a class nor an interface; it's a programming language.

"""
"""
QUESTION 1
----------
URL : http://www.greenstechnologys.com/

NOTE: Take screenshot of homepage.

"""
"""
from selenium import webdriver

# Set up the WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()

# Open the URL
driver.get("http://www.greenstechnologys.com/")

# Take a screenshot and save it with a specific name
driver.save_screenshot("homepage_screenshot.png")

# Close the browser
driver.quit()

"""
"""
QUESTION 2
----------
URL : http://toolsqa.com/

NOTE: Scrolldown till "Recent Articles".

"""
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()

# Open the URL
driver.get("http://toolsqa.com/")

# Wait for the page to load completely
time.sleep(2)

# Locate the "Recent Articles" section
recent_articles = driver.find_element(By.XPATH, "//*[text()='Recent Articles']")

# Scroll down to the "Recent Articles" section
driver.execute_script("arguments[0].scrollIntoView();", recent_articles)

# Optional: Pause to visually confirm the scroll
time.sleep(3)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 3
-----------
URL : http://toolsqa.com/

NOTE: Scrolldown till "Selenium Training Benefit" and print the word "Selenium Training Benefit"

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()

# Open the URL
driver.get("http://toolsqa.com/")

# Wait for the page to load completely
time.sleep(2)

# Locate the "Selenium Training Benefit" section
selenium_training = driver.find_element(By.XPATH, "//*[text()='Selenium Training Benefit']")

# Scroll down to the "Selenium Training Benefit" section
driver.execute_script("arguments[0].scrollIntoView();", selenium_training)

# Print the text of the section
print(selenium_training.text)

# Optional: Pause to visually confirm the scroll
time.sleep(3)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxx"""
"""
QUESTION 4
----------
URL : http://www.greenstechnologys.com/

NOTE: Scroll Down till "Greens technology Perumbakkam. address "and Take  screenshot 

"""
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()

# Open the URL
driver.get("http://www.greenstechnologys.com/")

# Wait for the page to load completely
time.sleep(2)

# Locate the "Greens technology Perumbakkam address" section
address_section = driver.find_element(By.XPATH, "//*[contains(text(), 'Greens technology Perumbakkam')]")

# Scroll down to the "Greens technology Perumbakkam address" section
driver.execute_script("arguments[0].scrollIntoView();", address_section)

# Wait for the scroll to complete
time.sleep(2)

# Take a screenshot and save it
driver.save_screenshot("perumbakkam_address_screenshot.png")

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxx"""