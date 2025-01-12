"""
SELENIUM
---------
DAY9
---------
Drop Down

"""
"""
What is the purpose of DropDown?

    A dropdown allows users to select one or more options from a predefined list.

How will you perform DropDown?

    By using the Select class in Selenium to interact with <select> elements.

What are the ways to select DropDown options?

    Using methods like select_by_visible_text(), select_by_index(), and select_by_value().

Whether Select is an interface or class?

    Select is a class in Selenium.

Write a code to print all the options in DropDown?

    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element(By.ID, "dropdownID"))
    for option in select.options:
        print(option.text)

Can we select multiple values in DropDown?

    Yes, but only if the <select> element has the multiple attribute.

How will you select multiple values in DropDown?

    By using select_by_index(), select_by_value(), or select_by_visible_text() for each option.

What are the methods available in Select class?

    Methods include select_by_index(), select_by_value(), select_by_visible_text(), deselect_by_index(), deselect_by_value(), deselect_by_visible_text(), deselect_all(), is_multiple(), and options.

Can we deselect the options in DropDown?

    Yes, if the dropdown supports multiple selections (has the multiple attribute).

Write a code to print selected options in DropDown?

    selected_options = select.all_selected_options

    for option in selected_options:
        print(option.text)

Write a code to deselect the selected options in DropDown?

    select.deselect_all()

"""
"""
QUESTION 1
----------
URL : http://demoqa.com/automation-practice-form/

NOTE: print all the even option in State and City

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demoqa.com/automation-practice-form/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Scroll down to make the dropdowns visible
    driver.execute_script("window.scrollTo(0, 500)")

    # Click on the "State" dropdown
    state_dropdown = driver.find_element(By.ID, "state")
    state_dropdown.click()
    time.sleep(1)  # Allow the options to load

    # Get all the State options
    state_options = driver.find_elements(By.XPATH, "//div[@id='state']//div[contains(@class,'menu')]/div")

    # Print even options from the State dropdown
    print("Even options in State dropdown:")
    for i in range(1, len(state_options), 2):  # Start from index 1 (2nd option) and skip alternately
        print(state_options[i].text)

    # Select a State to enable the City dropdown
    state_options[1].click()  # Selecting the 2nd option (even index 1)
    time.sleep(1)

    # Click on the "City" dropdown
    city_dropdown = driver.find_element(By.ID, "city")
    city_dropdown.click()
    time.sleep(1)  # Allow the options to load

    # Get all the City options
    city_options = driver.find_elements(By.XPATH, "//div[@id='city']//div[contains(@class,'menu')]/div")

    # Print even options from the City dropdown
    print("\nEven options in City dropdown:")
    for i in range(1, len(city_options), 2):  # Start from index 1 (2nd option) and skip alternately
        print(city_options[i].text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
----------
URL : http://demoqa.com/automation-practice-form/

NOTE: print all the odd option in State and City

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demoqa.com/automation-practice-form/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Scroll down to make the dropdowns visible
    driver.execute_script("window.scrollTo(0, 500)")

    # Click on the "State" dropdown
    state_dropdown = driver.find_element(By.ID, "state")
    state_dropdown.click()
    time.sleep(1)  # Allow the options to load

    # Get all the State options
    state_options = driver.find_elements(By.XPATH, "//div[@id='state']//div[contains(@class,'menu')]/div")

    # Print odd options from the State dropdown
    print("Odd options in State dropdown:")
    for i in range(0, len(state_options), 2):  # Start from index 0 (1st option) and skip alternately
        print(state_options[i].text)

    # Select a State to enable the City dropdown
    state_options[0].click()  # Selecting the 1st option (odd index 0)
    time.sleep(1)

    # Click on the "City" dropdown
    city_dropdown = driver.find_element(By.ID, "city")
    city_dropdown.click()
    time.sleep(1)  # Allow the options to load

    # Get all the City options
    city_options = driver.find_elements(By.XPATH, "//div[@id='city']//div[contains(@class,'menu')]/div")

    # Print odd options from the City dropdown
    print("\nOdd options in City dropdown:")
    for i in range(0, len(city_options), 2):  # Start from index 0 (1st option) and skip alternately
        print(city_options[i].text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 3
----------
URL : https://www.facebook.com/

NOTE: Print all the options in year using getAttirubute() method

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    time.sleep(3)  # Allow the page to load

    # Scroll down to the sign-up section
    driver.execute_script("window.scrollTo(0, 500)")

    # Find the "Year" dropdown
    year_dropdown = driver.find_element(By.ID, "year")

    # Get all the options within the "Year" dropdown
    year_options = year_dropdown.find_elements(By.TAG_NAME, "option")

    # Print all options using getAttribute()
    print("Options in the Year dropdown:")
    for option in year_options:
        print(option.get_attribute("value"))

finally:
    # Close the browser
    driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 4
----------
URL : https://www.facebook.com/

NOTE: Print all the options in month using getText() method

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    time.sleep(3)  # Allow the page to load

    # Scroll down to the sign-up section
    driver.execute_script("window.scrollTo(0, 500)")

    # Find the "Month" dropdown
    month_dropdown = driver.find_element(By.ID, "month")

    # Get all the options within the "Month" dropdown
    month_options = month_dropdown.find_elements(By.TAG_NAME, "option")

    # Print all options using getText()
    print("Options in the Month dropdown:")
    for option in month_options:
        print(option.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 5
-----------
URL : https://www.facebook.com/

NOTE: print the even dates

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    time.sleep(3)  # Allow the page to load

    # Scroll down to the sign-up section
    driver.execute_script("window.scrollTo(0, 500)")

    # Find the "Day" dropdown
    day_dropdown = driver.find_element(By.ID, "day")

    # Get all the options within the "Day" dropdown
    day_options = day_dropdown.find_elements(By.TAG_NAME, "option")

    # Print even dates
    print("Even dates in the Day dropdown:")
    for option in day_options:
        date = option.text
        if date.isdigit() and int(date) % 2 == 0:  # Check if the date is an even number
            print(date)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 6
-----------
URL : http://demo.guru99.com/test/newtours/register.php

NOTE: print all the option of country using getText() methods

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demo.guru99.com/test/newtours/register.php")
    driver.maximize_window()
    time.sleep(3)  # Allow the page to load

    # Find the "Country" dropdown
    country_dropdown = driver.find_element(By.NAME, "country")

    # Get all the options within the "Country" dropdown
    country_options = country_dropdown.find_elements(By.TAG_NAME, "option")

    # Print all options using getText()
    print("Options in the Country dropdown:")
    for option in country_options:
        print(option.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 7
-----------
URL : http://demo.guru99.com/test/newtours/register.php

NOTE: print all the option of country using getAttribute() method
      Register Form

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demo.guru99.com/test/newtours/register.php")
    driver.maximize_window()
    time.sleep(3)  # Allow the page to load

    # Find the "Country" dropdown
    country_dropdown = driver.find_element(By.NAME, "country")

    # Get all the options within the "Country" dropdown
    country_options = country_dropdown.find_elements(By.TAG_NAME, "option")

    # Print all options using getAttribute()
    print("Options in the Country dropdown using getAttribute():")
    for option in country_options:
        print(option.get_attribute("value"))

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 8
------------
URL : http://adactinhotelapp.com/

NOTE: Book room and print order no.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://adactinhotelapp.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Login to the website (use your valid credentials here)
    driver.find_element(By.ID, "username").send_keys("your_username")
    driver.find_element(By.ID, "password").send_keys("your_password")
    driver.find_element(By.ID, "login").click()
    time.sleep(3)  # Wait for login to complete

    # Fill in the hotel search form
    driver.find_element(By.ID, "location").send_keys("Sydney")
    driver.find_element(By.ID, "hotels").send_keys("Hotel Creek")
    driver.find_element(By.ID, "room_type").send_keys("Standard")
    driver.find_element(By.ID, "room_nos").send_keys("1")
    driver.find_element(By.ID, "datepick_in").send_keys("12/12/2025")
    driver.find_element(By.ID, "datepick_out").send_keys("14/12/2025")
    driver.find_element(By.ID, "adult_room").send_keys("2")
    driver.find_element(By.ID, "child_room").send_keys("0")
    driver.find_element(By.ID, "Submit").click()
    time.sleep(3)  # Wait for the search results to load

    # Select a hotel from the search results
    driver.find_element(By.ID, "radiobutton_0").click()  # Choose the first available hotel
    driver.find_element(By.ID, "continue").click()
    time.sleep(3)  # Wait for the booking form to load

    # Fill in the booking details (use valid data here)
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "address").send_keys("123 Main St, Sydney, Australia")
    driver.find_element(By.ID, "cc_num").send_keys("1234567812345678")  # Sample credit card number
    driver.find_element(By.ID, "cc_type").send_keys("VISA")
    driver.find_element(By.ID, "cc_exp_month").send_keys("12")
    driver.find_element(By.ID, "cc_exp_year").send_keys("2025")
    driver.find_element(By.ID, "cc_cvv").send_keys("123")
    driver.find_element(By.ID, "book_now").click()
    time.sleep(5)  # Wait for the booking confirmation page to load

    # Print the order number
    order_number = driver.find_element(By.XPATH, "//input[@name='order_no']").get_attribute("value")
    print("Booking Order Number:", order_number)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 9
-----------
URL : http://adactinhotelapp.com/

NOTE: print all the option in Room Type available.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://adactinhotelapp.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Login to the website (use your valid credentials here)
    driver.find_element(By.ID, "username").send_keys("your_username")
    driver.find_element(By.ID, "password").send_keys("your_password")
    driver.find_element(By.ID, "login").click()
    time.sleep(3)  # Wait for login to complete

    # Find the "Room Type" dropdown
    room_type_dropdown = driver.find_element(By.ID, "room_type")

    # Get all the options within the "Room Type" dropdown
    room_type_options = room_type_dropdown.find_elements(By.TAG_NAME, "option")

    # Print all options in the Room Type dropdown
    print("Options in the Room Type dropdown:")
    for option in room_type_options:
        print(option.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 10
-----------
URL : http://adactinhotelapp.com/

NOTE: print all the option in Location available.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://adactinhotelapp.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Login to the website (use your valid credentials here)
    driver.find_element(By.ID, "username").send_keys("your_username")
    driver.find_element(By.ID, "password").send_keys("your_password")
    driver.find_element(By.ID, "login").click()
    time.sleep(3)  # Wait for login to complete

    # Find the "Location" dropdown
    location_dropdown = driver.find_element(By.ID, "location")

    # Get all the options within the "Location" dropdown
    location_options = location_dropdown.find_elements(By.TAG_NAME, "option")

    # Print all options in the Location dropdown
    print("Options in the Location dropdown:")
    for option in location_options:
        print(option.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 11
-----------
URL : http://adactin.com/HotelApp/

NOTE: print No of option available in Adults per Room

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://adactin.com/HotelApp/")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Login to the website (use your valid credentials here)
    driver.find_element(By.ID, "username").send_keys("your_username")
    driver.find_element(By.ID, "password").send_keys("your_password")
    driver.find_element(By.ID, "login").click()
    time.sleep(3)  # Wait for login to complete

    # Find the "Adults per Room" dropdown
    adults_per_room_dropdown = driver.find_element(By.ID, "adult_room")

    # Get all the options within the "Adults per Room" dropdown
    adults_per_room_options = adults_per_room_dropdown.find_elements(By.TAG_NAME, "option")

    # Print the number of options available in the "Adults per Room" dropdown
    print("Number of options available in the 'Adults per Room' dropdown:", len(adults_per_room_options))

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 12
-----------
URL : http://output.jsbin.com/osebed/2

NOTE: Select Even Option availble in fruits
      Find out number of option not selected

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://output.jsbin.com/osebed/2")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Find the "Fruits" dropdown
    fruits_dropdown = driver.find_element(By.ID, "fruits")
    
    # Use the Select class to interact with the dropdown
    select = Select(fruits_dropdown)

    # Get all options in the dropdown
    options = select.options

    # Select even options (index 1, 3, 5, ...)
    for i in range(len(options)):
        if i % 2 != 0:  # Select the even options (index starts from 0)
            select.select_by_index(i)
    
    # Find the number of options that were not selected
    not_selected_count = len(options) - len(select.all_selected_options)

    # Print the number of options that were not selected
    print("Number of options not selected:", not_selected_count)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 13
-----------
URL : http://output.jsbin.com/osebed/2

NOTE: Select All availble in fruits
      Print first selected option 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://output.jsbin.com/osebed/2")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Find the "Fruits" dropdown
    fruits_dropdown = driver.find_element(By.ID, "fruits")
    
    # Use the Select class to interact with the dropdown
    select = Select(fruits_dropdown)

    # Select all available options
    for option in select.options:
        select.select_by_visible_text(option.text)
    
    # Print the first selected option
    first_selected_option = select.first_selected_option
    print("First selected option:", first_selected_option.text)

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxx"""
