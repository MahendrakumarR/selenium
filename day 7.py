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

"""
QUESTION 5
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: ScrollDown till "job opening" and Take the screenshot and  scroll up Online Classroom

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load
    
    # Step 2: Scroll down to "Job Opening"
    job_opening_element = driver.find_element(By.XPATH, "//h2[text()='Job Opening']")
    actions = ActionChains(driver)
    actions.move_to_element(job_opening_element).perform()
    time.sleep(2)  # Allow time for scrolling
    
    # Step 3: Take a screenshot
    driver.save_screenshot("job_opening_section.png")
    print("Screenshot of 'Job Opening' section saved.")
    
    # Step 4: Scroll back up to "Online Classroom"
    online_classroom_element = driver.find_element(By.XPATH, "//h2[text()='Online Classroom']")
    actions.move_to_element(online_classroom_element).perform()
    time.sleep(2)  # Allow time for scrolling
    
    print("Scrolled back up to 'Online Classroom' section.")
finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 6
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Scrolldown till "Top Selenium Trends In 2020" and takes Screenshot 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load
    
    # Step 2: Scroll down to "Top Selenium Trends In 2020"
    trends_element = driver.find_element(By.XPATH, "//h2[text()='Top Selenium Trends In 2020']")
    actions = ActionChains(driver)
    actions.move_to_element(trends_element).perform()
    time.sleep(2)  # Allow time for scrolling
    
    # Step 3: Take a screenshot
    driver.save_screenshot("selenium_trends_2020.png")
    print("Screenshot of 'Top Selenium Trends In 2020' section saved.")
    
finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 7
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click interviews question take the screenshot

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 2: Click on "Interviews Question"
    interviews_question_element = driver.find_element(By.XPATH, "//h2[contains(text(),'Interviews Questions')]")
    interviews_question_element.click()
    time.sleep(2)  # Wait for the content to load

    # Step 3: Take a screenshot
    driver.save_screenshot("interviews_question_section.png")
    print("Screenshot of 'Interviews Question' section saved.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxx"""
"""
QUESTION 8
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: In  CoreJava TestPaper Take the Screenshot 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 2: Scroll to and locate "Core Java Test Paper"
    core_java_element = driver.find_element(By.XPATH, "//h2[contains(text(),'Core Java Test Paper')]")
    actions = ActionChains(driver)
    actions.move_to_element(core_java_element).perform()
    time.sleep(2)  # Allow time for scrolling

    # Step 3: Click "Core Java Test Paper" (if it's a toggle)
    core_java_element.click()
    time.sleep(2)  # Wait for the content to load after clicking

    # Step 4: Take a screenshot
    driver.save_screenshot("core_java_test_paper.png")
    print("Screenshot of 'Core Java Test Paper' section saved.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION  9
------------
URL : https://www.flipkart.com/

NOTE: Search iphone and take the screenshot.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Flipkart URL
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Close the login popup if it appears
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_popup.click()
        time.sleep(1)
    except:
        print("Login popup not displayed.")

    # Step 3: Search for "iPhone"
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("iPhone")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for the search results to load

    # Step 4: Take a screenshot of the search results
    driver.save_screenshot("flipkart_iphone_search.png")
    print("Screenshot of iPhone search results saved.")

finally:
    # Close the browser
    driver.quit()
"""
"""
QUESTION 10
-----------
URL : https://www.amazon.in/

NOTE: Search motorolo and   take the screenshot.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Amazon India URL
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Locate the search bar and search for "Motorola"
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys("Motorola")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for the search results to load

    # Step 3: Take a screenshot of the search results
    driver.save_screenshot("amazon_motorola_search.png")
    print("Screenshot of Motorola search results saved.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 11
-----------
URL : https://www.flipkart.com/

NOTE: Mouse Over Kids & Baby  and Take the screenshot

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Flipkart URL
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Close the login popup if it appears
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_popup.click()
        time.sleep(1)
    except:
        print("Login popup not displayed.")

    # Step 3: Locate "Kids & Baby" and hover over it
    kids_baby_element = driver.find_element(By.XPATH, "//span[text()='Kids & Baby']")
    actions = ActionChains(driver)
    actions.move_to_element(kids_baby_element).perform()
    time.sleep(2)  # Allow time for the hover effect to appear

    # Step 4: Take a screenshot
    driver.save_screenshot("flipkart_kids_baby_hover.png")
    print("Screenshot of 'Kids & Baby' menu hover saved.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 12
-----------
URL : https://www.snapdeal.com/

NOTE: search HP laptop and take the screenshot .

"""
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Snapdeal URL
    driver.get("https://www.snapdeal.com/")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Locate the search bar and search for "HP Laptop"
    search_bar = driver.find_element(By.ID, "inputValEnter")
    search_bar.send_keys("HP Laptop")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for the search results to load

    # Step 3: Take a screenshot of the search results
    driver.save_screenshot("snapdeal_hp_laptop_search.png")
    print("Screenshot of HP Laptop search results saved.")

finally:
    # Close the browser
    driver.quit()
"""
"""
QUESTION 13
------------
URL : https://www.flipkart.com/

NOTE: Mouse Over Womens and take the screenshot.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Flipkart URL
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Step 2: Close the login popup if it appears
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_popup.click()
        time.sleep(1)
    except:
        print("Login popup not displayed.")

    # Step 3: Locate "Women" and hover over it
    women_element = driver.find_element(By.XPATH, "//span[text()='Women']")
    actions = ActionChains(driver)
    actions.move_to_element(women_element).perform()
    time.sleep(2)  # Allow time for the hover effect to appear

    # Step 4: Take a screenshot
    driver.save_screenshot("flipkart_women_hover.png")
    print("Screenshot of 'Women' menu hover saved.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxx"""