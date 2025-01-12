"""
DAY10
------------
Windows Handling

"""

"""
What is the purpose of windows Handling?

     Window handling allows you to switch between multiple windows or tabs in a browser during automation.

Write a code to perform windows Handling?

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

    # Open a new window/tab
    driver.execute_script("window.open('https://www.google.com', '_blank');")
    time.sleep(2)

    # Switch to the new window
    windows = driver.window_handles
    driver.switch_to.window(windows[1])  # Switching to the second window
    print(driver.title)

    # Switch back to the parent window
    driver.switch_to.window(windows[0])
    print(driver.title)

    driver.quit()

Which method is used to get parent window?

    driver.window_handles[0]

Which method is used to get child windows?

    driver.window_handles[1:] (or by using driver.switch_to.window(windows[index]))

Write a code to switch from parent window to child window?

    windows = driver.window_handles
    driver.switch_to.window(windows[1])  # Switch to the child window

In which order the windows order will arrange?

    The order is based on the sequence in which the windows are opened. The first opened window is the parent, and subsequent windows are child windows.

Write a code to return to your parent window?

    windows = driver.window_handles
    driver.switch_to.window(windows[0])  # Switch back to the parent window

What is the return type of getWindowHandles()?

    set (a set of window handles)

What is the return type of getWindowHandle()?

    string (the handle of the current window)

Write a code to switch to 8th child window?

    windows = driver.window_handles
    driver.switch_to.window(windows[7])  # Switch to the 8th child window (index starts from 0)

Write a code to switch to 8th child window without using any for loop?

    windows = driver.window_handles
    driver.switch_to.window(windows[7])  # Directly switch to the 8th child window

Write a code to switch multiple windows?

    windows = driver.window_handles
    for window in windows:
        driver.switch_to.window(window)
        print(driver.title)
"""
"""
QUESTION 1
----------
URL : https://www.amazon.com/

NOTE: Search iphones X and right click 1st phone and give open in new window 
      print cost of product

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open Amazon
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Search for iPhones X
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("iPhones X")
    search_box.submit()
    time.sleep(3)  # Wait for search results to load

    # Locate the first product
    first_product = driver.find_element(By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])[1]")

    # Perform a right-click action on the first product
    actions = ActionChains(driver)
    actions.context_click(first_product).perform()

    # Right-click and open the link in a new window (pressing 'T' will open in new tab on Windows)
    actions.send_keys('w').perform()
    time.sleep(3)  # Wait for the new window to open

    # Switch to the new window
    windows = driver.window_handles
    driver.switch_to.window(windows[1])  # Switch to the new window

    # Print the cost of the product
    price = driver.find_element(By.XPATH, "//span[@id='priceblock_ourprice' or @id='priceblock_dealprice']")
    print("Product price:", price.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
----------
URL : https://www.snapdeal.com/ 

NOTE: Search iphones 7 and click 1st phone 
      add it to cart.
      print the you pay cost displayed.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open Snapdeal
    driver.get("https://www.snapdeal.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Search for "iPhones 7"
    search_box = driver.find_element(By.ID, "inputValEnter")
    search_box.send_keys("iPhones 7")
    search_box.submit()
    time.sleep(3)  # Wait for the search results to load

    # Click on the first product
    first_product = driver.find_element(By.XPATH, "(//p[@class='product-title'])[1]")
    first_product.click()
    time.sleep(3)  # Wait for the product page to load

    # Click on 'Add to Cart'
    add_to_cart_button = driver.find_element(By.ID, "add-cart-button-id")
    add_to_cart_button.click()
    time.sleep(3)  # Wait for the product to be added to the cart

    # Navigate to the cart page
    cart_button = driver.find_element(By.ID, "cartOverlay")
    cart_button.click()
    time.sleep(3)  # Wait for the cart page to load

    # Get the "You Pay" cost
    you_pay_cost = driver.find_element(By.XPATH, "//span[@id='payAmount']")
    print("You Pay cost:", you_pay_cost.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 3
----------
URL : https://www.homedepot.com/

NOTE: Search celling fan 
      click 1st fan and click the remote control included

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open Home Depot website
    driver.get("https://www.homedepot.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Search for "ceiling fan"
    search_box = driver.find_element(By.ID, "headerSearch")
    search_box.send_keys("ceiling fan")
    search_box.submit()
    time.sleep(3)  # Wait for search results to load

    # Click on the first product in the search results
    first_product = driver.find_element(By.XPATH, "(//a[@class='product-pod--title'])[1]")
    first_product.click()
    time.sleep(3)  # Wait for the product page to load

    # Click on the "Remote Control Included" option if it exists
    try:
        remote_control_option = driver.find_element(By.XPATH, "//div[@class='product-attributes']//span[text()='Remote Control Included']")
        remote_control_option.click()
        time.sleep(2)  # Wait for the page to update
    except:
        print("Remote Control Included option not available.")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 4
----------
URL : http://www.greenstechnologys.com/python-training.html

NOTE: Click Selenium Test Papers and click Selenium Day10Task 
      Click Windows Handling and print 1 question 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://www.greenstechnologys.com/python-training.html")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Click on the "Selenium Test Papers" link
    selenium_test_papers = driver.find_element(By.LINK_TEXT, "Selenium Test Papers")
    selenium_test_papers.click()
    time.sleep(2)  # Wait for the page to load

    # Click on the "Selenium Day10Task" link
    selenium_day10_task = driver.find_element(By.LINK_TEXT, "Selenium Day10Task")
    selenium_day10_task.click()
    time.sleep(2)  # Wait for the page to load

    # Click on the "Windows Handling" link
    windows_handling = driver.find_element(By.LINK_TEXT, "Windows Handling")
    windows_handling.click()
    time.sleep(2)  # Wait for the page to load

    # Print the first question (Assuming it's in a specific tag like <h2>, <p>, etc.)
    first_question = driver.find_element(By.XPATH, "//p[starts-with(text(),'1.')]")  # Example XPath for the first question
    print("First Question:", first_question.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 5
----------
URL :  http://www.greenstechnologys.com/

NOTE: Mouse Over Course And click python 
      Right Click Explore Curriculum and click open in new window

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://www.greenstechnologys.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the "Course" element and perform mouse-over
    course_menu = driver.find_element(By.LINK_TEXT, "Course")
    actions = ActionChains(driver)
    actions.move_to_element(course_menu).perform()
    time.sleep(2)  # Allow the hover effect to trigger

    # Click on the "Python" link under "Course"
    python_course = driver.find_element(By.LINK_TEXT, "Python")
    python_course.click()
    time.sleep(3)  # Wait for the page to load

    # Right-click on "Explore Curriculum" and open in new window
    explore_curriculum = driver.find_element(By.LINK_TEXT, "Explore Curriculum")
    actions.context_click(explore_curriculum).perform()
    time.sleep(2)  # Wait for the context menu to appear

    # Simulate 'w' key press (to open in a new window/tab on most browsers)
    actions.send_keys('w').perform()
    time.sleep(3)  # Wait for the new window to open

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 6
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click Junit in Framework Test Paper
      print 1st Question in practical

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

    # Click on the "Junit" link under "Framework Test Paper"
    junit_link = driver.find_element(By.LINK_TEXT, "Junit")
    junit_link.click()
    time.sleep(3)  # Wait for the Junit page to load

    # Find and print the first question in the practical section
    # Assuming the questions are inside <p> tags or similar
    first_practical_question = driver.find_element(By.XPATH, "//p[starts-with(text(),'1.')]")  # Example XPath
    print("First Practical Question:", first_practical_question.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 7
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click Control Statement in Core Java Test Paper
      print 1st Question in Theorey

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

    # Click on the "Control Statement" link under "Core Java Test Paper"
    control_statement_link = driver.find_element(By.LINK_TEXT, "Control Statement")
    control_statement_link.click()
    time.sleep(3)  # Wait for the page to load

    # Find and print the first question in the Theory section
    # Assuming the questions are inside <p> tags or similar
    first_theory_question = driver.find_element(By.XPATH, "//p[starts-with(text(),'1.')]")  # Example XPath
    print("First Theory Question:", first_theory_question.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 8
----------
URL : https://www.snapdeal.com/ 

NOTE: Search hand sanitizer and click any hand sanitizer
      add it to cart
"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open Snapdeal website
    driver.get("https://www.snapdeal.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the search box and search for "hand sanitizer"
    search_box = driver.find_element(By.ID, "inputValEnter")
    search_box.send_keys("hand sanitizer")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for search results to load

    # Click on the first hand sanitizer in the search results
    first_hand_sanitizer = driver.find_element(By.XPATH, "(//a[@class='product-title'])[1]")
    first_hand_sanitizer.click()
    time.sleep(3)  # Wait for the product page to load

    # Click on the "Add to Cart" button
    add_to_cart_button = driver.find_element(By.XPATH, "//span[text()='Add to cart']")
    add_to_cart_button.click()
    time.sleep(2)  # Wait for the item to be added to the cart

    print("Item added to the cart successfully!")

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 9
----------
URL : https://www.flipkart.com/ 

NOTE: Search redmi phone and click any phone
      print price amount

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open Flipkart website
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Close the login popup if it appears
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_popup.click()
        time.sleep(1)
    except:
        pass  # If no popup appears, just continue

    # Locate the search box and search for "redmi phone"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("redmi phone")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for search results to load

    # Click on the first phone in the search results
    first_phone = driver.find_element(By.XPATH, "(//a[@class='_1fQZEK'])[1]")
    first_phone.click()
    time.sleep(3)  # Wait for the product page to load

    # Find and print the price of the phone
    price_element = driver.find_element(By.XPATH, "//div[@class='_30jeq3 _16Jk6d']")
    print("Price of the phone:", price_element.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 10
----------
URL : https://www.flipkart.com/ 

NOTE: Search mask and click any mask
      Enter delivery pincode

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open Flipkart website
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Close the login popup if it appears
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_popup.click()
        time.sleep(1)
    except:
        pass  # If no popup appears, just continue

    # Locate the search box and search for "mask"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("mask")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for search results to load

    # Click on the first mask in the search results
    first_mask = driver.find_element(By.XPATH, "(//a[@class='_1fQZEK'])[1]")
    first_mask.click()
    time.sleep(3)  # Wait for the product page to load

    # Locate the delivery pincode input field and enter a pincode
    pincode_field = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    pincode_field.send_keys("110001")  # Example pincode
    time.sleep(2)  # Wait for the pincode to be entered

    # Optionally, you can submit or take further actions here (e.g., check delivery availability)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 11
----------
URL : https://www.flipkart.com/ 

NOTE: Search hp laptop and click 1st hp laptop
      print cost of laptop

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open Flipkart website
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Close the login popup if it appears
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_popup.click()
        time.sleep(1)
    except:
        pass  # If no popup appears, just continue

    # Locate the search box and search for "hp laptop"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("hp laptop")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for search results to load

    # Click on the first HP laptop in the search results
    first_hp_laptop = driver.find_element(By.XPATH, "(//a[@class='_1fQZEK'])[1]")
    first_hp_laptop.click()
    time.sleep(3)  # Wait for the product page to load

    # Find and print the price of the laptop
    price_element = driver.find_element(By.XPATH, "//div[@class='_30jeq3 _16Jk6d']")
    print("Price of the laptop:", price_element.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 12
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click WindowsHandling in selenium Java Test Paper
      print question 13 in practic

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

    # Click on "WindowsHandling" link under "Selenium Java Test Paper"
    windows_handling_link = driver.find_element(By.LINK_TEXT, "WindowsHandling")
    windows_handling_link.click()
    time.sleep(3)  # Wait for the page to load

    # Find and print question 13 under the "Practical" section
    # Assuming the question is within a <p> tag or similar
    question_13 = driver.find_element(By.XPATH, "//p[contains(text(),'13.')]")  # Example XPath
    print("Question 13 in Practical:", question_13.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 13
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click Testng in Framework Test Paper
      print 4th  Question in practical

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

    # Click on "Testng" link under "Framework Test Paper"
    testng_link = driver.find_element(By.LINK_TEXT, "Testng")
    testng_link.click()
    time.sleep(3)  # Wait for the page to load

    # Find and print the 4th question under the "Practical" section
    # Assuming the question is within a <p> tag or similar
    question_4 = driver.find_element(By.XPATH, "//p[contains(text(),'4.')]")  # Example XPath
    print("4th Question in Practical:", question_4.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxx"""