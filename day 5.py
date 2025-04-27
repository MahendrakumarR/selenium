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
    amount_debit = driver.find_element(By.XPATH, "//li[@id='fourth']/a")
    debit_amount = driver.find_element(By.XPATH, "//ol[@id='amt7']/li") 
    actions.drag_and_drop(amount_debit, debit_amount).perform()
    print("Dragged '5000' to 'Amount' at the debited side.")

    
    # Drag 'SALES' to 'Account' (Credited Side)
    sales = driver.find_element(By.XPATH, "//li[@id='credit1']/a")
    credit_account = driver.find_element(By.XPATH, "//ol[@id='loan']/li")
    actions.drag_and_drop(sales, credit_account).perform()
    print("Dragged 'SALES' to 'Account' at the credited side.")

    # Drag '5000' to 'Amount' (Credited Side)
    amount_5000_credit = driver.find_element(By.XPATH, "//li[@id='fourth']/a")
    credit_amount = driver.find_element(By.XPATH, "//ol[@id='amt8']/li")
    actions.drag_and_drop(amount_5000_credit, credit_amount).perform()
    print("Dragged '5000' to 'Amount' at the credited side.")
    
    
except Exception as e:
    print("Error during drag and drop:", e)

# Close the WebDriver
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

xxxxxxxxxxxxxxxxxxxxxxxxx"""

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
    home_furniture = driver.find_element(By.XPATH, "//span[text()='Home & Furniture']")

    # Perform mouse-over on "Home & Furniture"
    actions.move_to_element(home_furniture).perform()
    print("Mouse-over on 'Home & Furniture' completed.")


    # Wait for the dropdown to appear
    time.sleep(2)
    
    # Locate and click "Bath Towels" in the dropdown
    bath_towels = driver.find_element(By.XPATH, "//a[contains(text(), 'Cleaning & Bath')]")
    bath_towels.click()
    print("Clicked 'Bath Towels' successfully.")
    
    # Wait for the Bath Towels page to load
    time.sleep(3)
    
    # Get the name of the first product displayed
    product_name = driver.find_element(By.XPATH, "//a[text()='Mops']")
    product_name.click()
    print("First product name in 'Bath Towels' category:")

except Exception as e:
    print("Error:", e)

# Close the WebDriver
driver.quit()

xxxx Last line name not get """

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
driver = webdriver.Firefox()

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

xxxxxxxxxxxxx"""
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
driver = webdriver.Firefox()

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

"""

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
driver = webdriver.Firefox()

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
software_testing_training = driver.find_element("xpath", "//span[text()='Software Testing (12)']")

# Perform mouseover on the "Software Testing Training" submenu
action.move_to_element(software_testing_training).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "Selenium Training" link
selenium_training = driver.find_element("xpath", "//span[text()='Selenium Certification Training']")
selenium_training.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

"""

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
driver = webdriver.Firefox()

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
oracle_training = driver.find_element("xpath", "//span[text()='Oracle (48)']")

# Perform mouseover on the "Oracle Training" submenu
action.move_to_element(oracle_training).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "Oracle SQL Training" link
oracle_sql_training = driver.find_element("xpath", "//span[text()='Oracle SQL and PLSQL Placement Certification Training']")
oracle_sql_training.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

"""

"""

QUESTION 8
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Courses  is first mouseover
      DataWarehouse training is second mouse over
      click microstategy training.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

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

# Locate the "Data Warehouse Training" submenu
data_warehouse_training = driver.find_element("xpath", "//span[text()='Data Warehousing (5)']")

# Perform mouseover on the "Data Warehouse Training" submenu
action.move_to_element(data_warehouse_training).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "MicroStrategy Training" link
microstrategy_training = driver.find_element("xpath", "//span[text()='COGNOS TM1 Certification Training']")
microstrategy_training.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()
"""

"""
QUESTION 9
-----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Courses  is first mouseover
      RPA is second mouseover
      Click Blue prism Certification training

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

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

# Locate the "RPA" submenu
rpa_menu = driver.find_element("xpath", "//span[text()='RPA (6)']")

# Perform mouseover on the "RPA" submenu
action.move_to_element(rpa_menu).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "Blue Prism Certification Training" link
blue_prism_training = driver.find_element("xpath", "//span[text()='Blue Prism Certification Training']")
blue_prism_training.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()
"""

"""
QUESTION 10
-----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Courses is first mouseover
      Data Warehousing is second mouseover

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

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

# Locate the "Data Warehousing" submenu
data_warehousing_menu = driver.find_element("xpath", "//span[text()='Data Warehousing (5)']")

# Perform mouseover on the "Data Warehousing" submenu
action.move_to_element(data_warehousing_menu).perform()

# Add a short delay to observe the submenu
time.sleep(3)

# Close the browser
driver.quit()

"""

"""
QUESTION 11
-----------
URL : https://www.homedepot.com/

NOTE: Alldepartment  is first mouseover
      Heating and cooling  is second  mouseover
      Air conditioners is third mouseover 
      Click portable air conditioners.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.homedepot.com/"
driver.get(url)

# block pop-ups
options = Options()
options.set_preference("dom.disable_open_during_load", True)
driver = webdriver.Firefox(options=options)

# Maximize the browser window
driver.maximize_window()

time.sleep(3)

# Locate the "All Departments" menu
all_departments = driver.find_element("xpath", "//button[@aria-label='open drawer to view Shop All']")

# Perform mouseover on "All Departments"
action = ActionChains(driver)
action.move_to_element(all_departments).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

depart = driver.find_element("xpath", "//span[text()='Shop By Department']")
action.move_to_element(depart).perform()

time.sleep(2)
# Locate the "Heating & Cooling" submenu
heating_and_cooling = driver.find_element("xpath", "//span[text()='Heating, Cooling, & Air Quality']")

# Perform mouseover on "Heating & Cooling"
action.move_to_element(heating_and_cooling).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate the "Air Conditioners" submenu
air_conditioners = driver.find_element("xpath", "//span[text()='Air Conditioners']")

# Perform mouseover on "Air Conditioners"
action.move_to_element(air_conditioners).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "Portable Air Conditioners" link
portable_air_conditioners = driver.find_element("xpath", "//span[text()='Portable Air Conditioners']")
portable_air_conditioners.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

XXXXXXXXXXXXXX """ 

""" 
QUESTION 12
-----------
URL : https://www.homedepot.com/ 

NOTE: All department is first mouseover 
      Paint is second mouseover
      Interior painting is third mouseover
      Click celling paint.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.homedepot.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Locate the "All Departments" menu
all_departments = driver.find_element("xpath", "//a[@data-id='departmentsFlyout']")

# Perform mouseover on "All Departments"
action = ActionChains(driver)
action.move_to_element(all_departments).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate the "Paint" submenu
paint_menu = driver.find_element("xpath", "//a[text()='Paint']")

# Perform mouseover on "Paint"
action.move_to_element(paint_menu).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate the "Interior Painting" submenu
interior_painting = driver.find_element("xpath", "//a[text()='Interior Painting']")

# Perform mouseover on "Interior Painting"
action.move_to_element(interior_painting).perform()

# Add a short delay to ensure the next submenu loads
time.sleep(2)

# Locate and click the "Ceiling Paint" link
ceiling_paint = driver.find_element("xpath", "//a[text()='Ceiling Paint']")
ceiling_paint.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxx"""
"""

QUESTION 13
-----------
URL :  https://www.snapdeal.com/

NOTE:  Mobile & Tablets is first mouseover
       Click newly lanuch covers.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.snapdeal.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Locate the "Mobile & Tablets" menu
mobile_and_tablets_menu = driver.find_element("xpath", "//span[text()='Mobile & Accessories']")

# Perform mouseover on the "Mobile & Tablets" menu
action = ActionChains(driver)
action.move_to_element(mobile_and_tablets_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate the "Newly Launch Covers" link
newly_launch_covers = driver.find_element("xpath", "//span[text()='Printed Back Covers']")

# Click on the "Newly Launch Covers" link
newly_launch_covers.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

"""

"""

QUESTION 14
-----------
URL : https://www.snapdeal.com/

NOTE: Women's Fashion is first mouseover
      Click footwear->click heals.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.snapdeal.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Locate the "Women's Fashion" menu                 
womens_fashion_menu = driver.find_element("xpath", '//span[text()="Women\'s Fashion"]')

# Perform mouseover on the "Women's Fashion" menu
action = ActionChains(driver)
action.move_to_element(womens_fashion_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate and click the "Footwear" link
footwear_link = driver.find_element("xpath", "//span[text()='Heels']")

# Click on the "Footwear" link
footwear_link.click()

# Add a short delay to ensure the page loads
time.sleep(3)

# Close the browser
driver.quit()

"""
"""

QUESTION 15
-----------
URL : https://www.amazon.in/

NOTE: Signin is first mouseover
      Click Register
      Give details for Register

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.amazon.in/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Locate the "Sign In" menu
sign_in_menu = driver.find_element("xpath", "//a[@data-nav-ref='nav_ya_signin']")

# Perform mouseover on the "Sign In" menu
action = ActionChains(driver)
action.move_to_element(sign_in_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate and click the "Start here" (Register) link
register_link = driver.find_element("xpath", "//a[text()='Start here.']")

# Click on the "Register" link
register_link.click()

# Add a short delay to ensure the Register page loads
time.sleep(3)

# Locate the email input field and enter an email
email_input = driver.find_element("xpath", "//input[@name='email']")
email_input.send_keys("8056769187")


# Locate the password check field and re-enter the password
continue_ = driver.find_element("xpath", "//span[@id='continue']")
continue_.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()
"""

"""
QUESTON 16
----------
URL : https://www.amazon.in/

NOTE: signin is a first mouseover
      Click SD Cash

"""
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.amazon.in/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(2)

# Locate the "Sign In" menu
sign_in_menu = driver.find_element("xpath",'//input[@id="twotabsearchtextbox"]')
sign_in_menu.send_keys("sd cash")
sign_in_menu.send_keys(Keys.ENTER)

time.sleep(15)

driver.quit()

"""

"""
QUESTION 17
-----------
URL : https://www.flipkart.com/

NOTE: womens is mouseover
      Click flat slipper

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.flipkart.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Close the login popup if it appears
try:
    close_popup = driver.find_element("xpath", "//button[contains(text(), '✕')]")
    close_popup.click()
    time.sleep(2)
except:
    pass

# Locate the "fashion" menu
fashion = driver.find_element("xpath", "//span[text()='Fashion']")

# Perform mouseover on the "Womens" menu
action = ActionChains(driver)
action.move_to_element(fashion).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate and click the "womens foot wear" category
foot_wear = driver.find_element("xpath", "//a[text()='Women Footwear']")
action = ActionChains(driver)
action.move_to_element(foot_wear).perform()

flat = driver.find_element("xpath", "//a[text()='Women Flats']")
flat.click()

# Add a short delay to observe the result   
time.sleep(5)

# Close the browser
driver.quit()
"""


"""
QUESTION 18
-----------
URL : https://www.flipkart.com/

NOTE: Baby&Kids is mouseover
      Click Remote Control Toys

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.flipkart.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Close the login popup if it appears
try:
    close_popup = driver.find_element("xpath", "//button[contains(text(), '✕')]")
    close_popup.click()
    time.sleep(2)
except:
    pass

# Locate the "Baby & Kids" menu
baby_and_kids_menu = driver.find_element("xpath", "//span[text()='Beauty, Toys & More']")

# Perform mouseover on the "Baby & Kids" menu
action = ActionChains(driver)
action.move_to_element(baby_and_kids_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

toys = driver.find_element("xpath", "//a[text()='Toys & School Supplies']")
action = ActionChains(driver)
action.move_to_element(toys).perform()

# Locate and click the "Remote Control Toys" category
remote_control_toys_link = driver.find_element("xpath", "(//a[@class='_3490ry'])[1]")

# Click on the "Remote Control Toys" link
remote_control_toys_link.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

"""

"""
QUESTION 19
-----------
URL : https://www.flipkart.com/

NOTE: Electronics is mouseover
      Click Realme
      Click 1st Product name

"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the specified URL
url = "https://www.flipkart.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Close the login popup if it appears
try:
    close_popup = driver.find_element("xpath", "//button[contains(text(), '✕')]")
    close_popup.click()
    time.sleep(2)
except:
    pass

# Locate the "Electronics" menu
electronics_menu = driver.find_element("xpath", "//div[text()='Electronics']")

# Perform mouseover on the "Electronics" menu
action = ActionChains(driver)
action.move_to_element(electronics_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate and click the "Realme" link
realme_link = driver.find_element("xpath", "//a[text()='Realme']")
realme_link.click()

# Add a short delay to ensure the page loads with products
time.sleep(3)

# Locate and click the first product name on the page
first_product = driver.find_element("xpath", "(//a[@class='_1fQZEK'])[1]")

# Click on the first product
first_product.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()



"""
QUESTION 20
-----------
URL : https://www.flipkart.com/

NOTE: Tvs & Appliances  is mouseover
      Click Mi
      Click 1st Product name

"""
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the specified URL
url = "https://www.flipkart.com/"
driver.get(url)

# Maximize the browser window
driver.maximize_window()

# Add a short delay to allow the page to load completely
time.sleep(5)

# Close the login popup if it appears
try:
    close_popup = driver.find_element("xpath", "//button[contains(text(), '✕')]")
    close_popup.click()
    time.sleep(2)
except:
    pass

# Locate the "TVs & Appliances" menu
tvs_and_appliances_menu = driver.find_element("xpath", "//div[text()='TVs & Appliances']")

# Perform mouseover on the "TVs & Appliances" menu
action = ActionChains(driver)
action.move_to_element(tvs_and_appliances_menu).perform()

# Add a short delay to ensure the submenu loads
time.sleep(2)

# Locate and click the "Mi" link
mi_link = driver.find_element("xpath", "//a[text()='Mi']")
mi_link.click()

# Add a short delay to ensure the page loads with products
time.sleep(3)

# Locate and click the first product name on the page
first_product = driver.find_element("xpath", "(//a[@class='_1fQZEK'])[1]")

# Click on the first product
first_product.click()

# Add a short delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxx"""