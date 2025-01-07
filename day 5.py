"""
DAY 5
---------------
Actions(mouseOver action,drag and drop)

"""

"""
What is MouseOverAction?
    
    MouseOverAction simulates hovering the mouse over a specific web element.

Write a code to perform MouseOverAction?

    from selenium.webdriver import ActionChains
    action = ActionChains(driver)
    action.move_to_element(element).perform()

Whether Action is a class or Interface?
    
    Action is an interface in Selenium.

How will you perform Drag and Drop?

    Use action.drag_and_drop(source, target).perform() from the ActionChains class.

What is the use of the Action class?

    The Action class is used to perform advanced user interactions like mouse and keyboard actions.

What is the purpose of Drag and Drop?

    Drag and Drop allows moving an element from one location to another.

In which class dragAndDrop method is available?

    The dragAndDrop method is available in the ActionChains class.

Why we use .perform()?
    .perform() executes the sequence of actions defined in ActionChains.

What is the purpose of moveToElement()? Where is it used?

    moveToElement() moves the mouse pointer to a specific element; used for hover actions.

In which class moveToElement() is present?

    The moveToElement() method is present in the ActionChains class.

How will you perform MouseOver action?

    Use action.move_to_element(element).perform() from ActionChains.

What is the difference between moveToElement() & switchTo()?

    moveToElement() interacts with elements via mouse; switchTo() handles frames, alerts, or windows.

"""
"""
QUESTION 1
----------
URL : http://demo.guru99.com/test/drag_drop.html 

NOTE: Drag and drop  bank  in Account ,5000 in amount  at debited side 
      Drag and drop  sales in Account ,5000 in amount  at credited side 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://demo.guru99.com/test/drag_drop.html")

# Wait for the page to load
time.sleep(2)

# Initialize ActionChains
actions = ActionChains(driver)

# Locate the source and target elements
try:
    # Drag 'BANK' to 'Account' (Debited Side)
    bank = driver.find_element(By.XPATH, "//a[contains(text(),'BANK')]")
    debit_account = driver.find_element(By.XPATH, "//ol[@id='bank']/li")
    actions.drag_and_drop(bank, debit_account).perform()
    print("Dragged 'BANK' to 'Account' at the debited side.")

    # Drag '5000' to 'Amount' (Debited Side)
    amount_5000_debit = driver.find_element(By.XPATH, "//a[contains(text(),'5000') and @class='placeholder']")
    debit_amount = driver.find_element(By.XPATH, "//ol[@id='amt7']/li")
    actions.drag_and_drop(amount_5000_debit, debit_amount).perform()
    print("Dragged '5000' to 'Amount' at the debited side.")

    # Drag 'SALES' to 'Account' (Credited Side)
    sales = driver.find_element(By.XPATH, "//a[contains(text(),'SALES')]")
    credit_account = driver.find_element(By.XPATH, "//ol[@id='loan']/li")
    actions.drag_and_drop(sales, credit_account).perform()
    print("Dragged 'SALES' to 'Account' at the credited side.")

    # Drag '5000' to 'Amount' (Credited Side)
    amount_5000_credit = driver.find_element(By.XPATH, "//a[contains(text(),'5000') and @class='placeholder']")
    credit_amount = driver.find_element(By.XPATH, "//ol[@id='amt8']/li")
    actions.drag_and_drop(amount_5000_credit, credit_amount).perform()
    print("Dragged '5000' to 'Amount' at the credited side.")

except Exception as e:
    print("Error during drag and drop:", e)

# Close the WebDriver
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
-----------
URL:  http://www.amazon.in

NOTE: Try Prime first mouseover
      Click Free fast delievery on prime items

"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://www.amazon.in")

# Maximize the browser window
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Initialize ActionChains
actions = ActionChains(driver)

try:
    # Locate the "Try Prime" menu
    try_prime = driver.find_element(By.ID, "nav-link-amazonprime")
    
    # Perform mouse-over on "Try Prime"
    actions.move_to_element(try_prime).perform()
    print("Mouse-over on 'Try Prime' completed.")
    
    # Wait for the dropdown to appear
    time.sleep(2)
    
    # Locate and click "Free fast delivery on Prime items"
    free_fast_delivery = driver.find_element(By.XPATH, "//a[contains(text(), 'Free fast delivery on Prime items')]")
    free_fast_delivery.click()
    print("Clicked 'Free fast delivery on Prime items' successfully.")

except Exception as e:
    print("Error:", e)

# Close the WebDriver
driver.quit()

xxxxxxxxxxxxxxxx"""

"""
QUESTION 3
----------
URL : http://www.flipkart.com

NOTE: Home & Furniture is first mouseover 
      Click Bath Towels and print any product name 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Flipkart URL
driver.get("http://www.flipkart.com")

# Maximize the browser window
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Initialize ActionChains
actions = ActionChains(driver)

try:
    # Locate the "Home & Furniture" menu
    home_furniture = driver.find_element(By.XPATH, "//div[text()='Home & Furniture']")
    
    # Perform mouse-over on "Home & Furniture"
    actions.move_to_element(home_furniture).perform()
    print("Mouse-over on 'Home & Furniture' completed.")
    
    # Wait for the dropdown to appear
    time.sleep(2)
    
    # Locate and click "Bath Towels" in the dropdown
    bath_towels = driver.find_element(By.XPATH, "//a[contains(text(), 'Bath Towels')]")
    bath_towels.click()
    print("Clicked 'Bath Towels' successfully.")
    
    # Wait for the Bath Towels page to load
    time.sleep(3)
    
    # Get the name of the first product displayed
    product_name = driver.find_element(By.XPATH, "(//a[@class='_1fQZEK'])[1]").text
    print("First product name in 'Bath Towels' category:", product_name)

except Exception as e:
    print("Error:", e)

# Close the WebDriver
driver.quit()
xxxxxxxxxxxxxxxxxxxx"""

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
import time

# Initialize the driver
driver = webdriver.Chrome()

# Open the ShopClues website
url = "https://www.shopclues.com/wholesale.html"
driver.get(url)

# Maximize the window
driver.maximize_window()

# Add a short delay to allow the page to load
time.sleep(3)

# Locate the "Mobile and Electronics" menu
mobile_and_electronics = driver.find_element("xpath", "//a[contains(text(), 'Mobiles & Electronics')]")

# Perform mouseover action
action = ActionChains(driver)
action.move_to_element(mobile_and_electronics).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate and click the "Smart Phones Range Rs5001 - Rs10000" link
smartphones_range = driver.find_element("xpath", "//a[contains(text(), 'Smartphones Range Rs5001 - Rs10000')]")
smartphones_range.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxx"""

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
import time

# Initialize the driver
driver = webdriver.Chrome()

# Open the ShopClues website
url = "https://www.shopclues.com/wholesale.html"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(3)

# Locate the "Sports & More" menu
sports_and_more = driver.find_element("xpath", "//a[contains(text(), 'Sports & More')]")

# Perform mouseover action
action = ActionChains(driver)
action.move_to_element(sports_and_more).perform()

# Add a short delay to ensure the submenu appears
time.sleep(2)

# Locate and click the "Weights Grainers" link
weights_trainers = driver.find_element("xpath", "//a[contains(text(), 'Weights Grainers')]")
weights_trainers.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 6 
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Course is first mouseover
      Software testing training is second mouseover  
      Click selenium training 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the specified URL
url = "http://greenstech.in/selenium-course-content.html"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(3)

# Locate the "Course" menu
course_menu = driver.find_element("xpath", "//div[contains(text(), 'Course')]")

# Perform mouseover on the "Course" menu
action = ActionChains(driver)
action.move_to_element(course_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate the "Software Testing Training" submenu
software_testing_training = driver.find_element("xpath", "//span[text()='Software Testing Training']")

# Perform mouseover on the "Software Testing Training" submenu
action.move_to_element(software_testing_training).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "Selenium Training" link
selenium_training = driver.find_element("xpath", "//span[text()='Selenium Training']")
selenium_training.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 7
-----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Courses is first mouseover
      Oracle training is second mouseover
      Click Oracle sql training

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the specified URL
url = "http://greenstech.in/selenium-course-content.html"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(3)

# Locate the "Courses" menu
courses_menu = driver.find_element("xpath", "//div[contains(text(), 'Courses')]")

# Perform mouseover on the "Courses" menu
action = ActionChains(driver)
action.move_to_element(courses_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate the "Oracle Training" submenu
oracle_training = driver.find_element("xpath", "//span[text()='Oracle Training']")

# Perform mouseover on the "Oracle Training" submenu
action.move_to_element(oracle_training).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "Oracle SQL Training" link
oracle_sql_training = driver.find_element("xpath", "//span[text()='Oracle SQL Training']")
oracle_sql_training.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 8
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Courses  is first mouseover
      DataWarehouse training is second mouse over
      click microstategy training.

"""
