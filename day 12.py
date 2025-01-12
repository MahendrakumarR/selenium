"""
DAY12:
-----
JavaScript

"""

"""
What is mean by JavaScript?

    JavaScript is a programming language used to create dynamic content on web pages.

Whether JavaScript is a class or Interface?

    JavaScript is neither a class nor an interface; it's a programming language.

What is the method available to run the Javascript?

    executeScript() method in Selenium is used to run JavaScript.

Write a code to click a button using JavaScript?

    document.getElementById("buttonId").click();

Write a code to insert a value in textBox using JavaScript?

    document.getElementById("textBoxId").value = "someValue";

What method is used to get the font size of the WebElement in a webpage?
    
    getComputedStyle(element).fontSize

What method is used to get the Color of the WebElement in a webpage?

    getComputedStyle(element).color

Write a code to highlight the WebElement in a webpage?

    arguments[0].style.border = "3px solid red";

Write a code to get the InnerText and Title of a webpage using Javascript?

    var innerText = document.body.innerText; var title = document.title;

Write a code to perform scrollUp in a webpage using Javascript?

    window.scrollBy(0, -window.innerHeight);

Write a code to perform scrolldown in a webpage using Javascript?

    window.scrollBy(0, window.innerHeight);

"""

"""
QUESTION 1
-----------
URL : http://www.greenstechnologys.com/

NOTE: Go to down of the webpage using scrolldown and print the line 
"Greens Technologies Porur
149, 1C/1D, 1st Floor,
Opp to DLF IT Park,
Ramapuram,
Chennai - 600089."

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://www.greenstechnologys.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Scroll down to the bottom of the page using JavaScript
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load after scrolling

    # Locate the element with the text and print it
    address_text = driver.find_element(By.XPATH, "//p[contains(text(), 'Greens Technologies Porur')]").text
    print(address_text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
-----------
URL : http://toolsqa.com/

NOTE: Go to "Share this page" using scrolldown and again "Latest Tutorials" using scrollup.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://toolsqa.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Scroll down to "Share this page"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load after scrolling

    # Locate "Share this page" and perform a scroll to that section
    share_section = driver.find_element(By.XPATH, "//span[text()='Share this page']")
    driver.execute_script("arguments[0].scrollIntoView();", share_section)
    time.sleep(2)

    # Scroll up to "Latest Tutorials"
    latest_tutorials = driver.find_element(By.XPATH, "//span[text()='Latest Tutorials']")
    driver.execute_script("arguments[0].scrollIntoView();", latest_tutorials)
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 3
-----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Scroll Till Framework Test Papers

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the "Framework Test Papers" section and scroll to it
    framework_section = driver.find_element(By.XPATH, "//span[text()='Framework Test Papers']")
    driver.execute_script("arguments[0].scrollIntoView();", framework_section)
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxx"""