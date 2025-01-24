
"""
DAY4
------------
Debug 
Xpath contains,text
getText();
getAttribute()

"""
"""
What is the purpose of debug?

    Debugging is used to identify and fix issues or bugs in the code to ensure the program runs correctly.

What are the steps for debugging?

    Reproduce the error, isolate the issue, check logs, use a debugger, fix the bug, and test the solution.

What are the types of debug?

    Manual, automated, interactive, and remote debugging.

How to take a locator in which contains no tag?

    Use attributes like id, class, or name in an XPath or CSS selector (e.g., //*[contains(@class, 'value')]).

How to print a paragraph from a webpage?

    Use driver.find_element(By.TAG_NAME, 'p').text to print the paragraph text.

What are the methods to get and print the text from a webpage?

    Use element.text to get text and element.get_attribute('attribute_name') to get attribute values.

What is the purpose of getText() and getAttribute()?

    getText() retrieves visible text, while getAttribute() retrieves the value of an element's attribute.

What is the return type of getText() and getAttribute()?

    Both return a string.

In which interface are getText() and getAttribute() available?

    They are available in the WebElement interface.

What are the differences between getText() and getAttribute()?

    getText() retrieves visible text, while getAttribute() retrieves attribute values (e.g., value, href).

Is it possible to get the text from a webpage without using getText()?

    Yes, you can use getAttribute('innerText') or getAttribute('textContent') to get text.

"""
"""
QUESTION 1
----------
URL : http://www.greenstechnologys.com 

NOTE: Print Greens Technologys Software Training Centers in Chennai

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://www.greenstechnologys.com")

# Locate all div elements that might contain the center names (adjusted to match the right structure)
centers = driver.find_elements(By.XPATH, "//div[@class='col-md-4']//p")

# Print the center names
for center in centers:
    print(center.text)

# Close the WebDriver
driver.quit()

xxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Print paragaraph starts with vel murugan.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://greenstech.in/selenium-course-content.html")

try:
    # Locate and switch to the iframe
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    print("Switched to iframe successfully.")

    # Debug: Print all paragraphs inside the iframe
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for index, paragraph in enumerate(paragraphs):
        print(f"Paragraph {index}: {paragraph.text}")

    # Wait for the desired paragraph
    paragraph = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Vel Murugan')]"))
    ).text
    print("Found paragraph:", paragraph)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Switch back to the main content and close WebDriver
    driver.switch_to.default_content()
    driver.quit()

"""

"""
QUESTION 3
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Print the adayar branch address

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://greenstech.in/selenium-course-content.html")

adyar = driver.find_element(By.XPATH,"//span[contains(text(),'Adyar')]")
no = driver.find_element(By.XPATH,"//span[contains(text(),'No:11,')]")
street = driver.find_element(By.XPATH,"//span[contains(text(),'First Street,')]")
nagar = driver.find_element(By.XPATH,"//span[contains(text(),'padmanabha Nagar,')]")
ad = driver.find_element(By.XPATH,"//span[contains(text(),'Adyar,')]")
chennai = driver.find_element(By.XPATH,"//span[contains(text(),'Chennai-600 020.')]")
ph = driver.find_element(By.XPATH, "//h6[contains(text(), 'Greens Technology') and contains(text(), 'Adyar')]//following::p[contains(@class, 'center-contact')]//a")
mail = driver.find_element(By.XPATH,"//a[contains(text(),'contact@greenstechnologys.com')]")

print(adyar.text)
print(no.text)
print(street.text)
print(nagar.text)
print(ad.text)
print(chennai.text)
print("phone:",ph.text)
print(mail.text)



"""
QUESTION 4
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Print the omr branch address

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://greenstech.in/selenium-course-content.html")

# Locate the OMR branch address
try:
    address = driver.find_element(By.XPATH, "//p[contains(text(), 'OMR')]").text
    print("OMR Branch Address:", address)
except Exception as e:
    print("Error locating the OMR branch address:", e)

# Close the WebDriver
driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 5
----------
URL : http://www.greenstechnologys.com/

NOTE: Print the paragraph starts with Greens Technology

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://www.greenstechnologys.com/")

# Locate the paragraph starting with "Greens Technology"
try:
    paragraph = driver.find_element(By.XPATH, "//p[starts-with(text(), 'Greens Technology')]").text
    print("Paragraph:", paragraph)
except Exception as e:
    print("Error locating the paragraph:", e)

# Close the WebDriver
driver.quit()
xxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 6
----------
URL : https://www.facebook.com/ 

NOTE: Print the email and password which was entered by user 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Facebook URL
driver.get("https://www.facebook.com/")

# Wait for the page to load
time.sleep(3)  # Add a delay to ensure elements are loaded (use WebDriverWait for better practice)

# Enter sample email and password
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")

# Input email and password
email_field.send_keys("example_user@gmail.com")
password_field.send_keys("example_password123")

# Retrieve and print the entered values
email_value = email_field.get_attribute("value")
password_value = password_field.get_attribute("value")

print("Entered Email:", email_value)
print("Entered Password:", password_value)

# Close the WebDriver
driver.quit()

"""
"""
QUESTION 7
----------
URL : http://www.google.com/

NOTE: Search greens velmurugan and click the 1st link.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Google URL
driver.get("http://www.google.com/")

# Locate the search bar and enter the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("greens velmurugan")  # Enter search query
search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

# Wait for the search results to load
time.sleep(3)

# Click the first link in the search results
try:
    first_link = driver.find_element(By.XPATH, "(//h3)[1]")  # Locate the first link using its <h3> tag
    first_link.click()
    print("Successfully clicked the first link.")
except Exception as e:
    print("Error clicking the first link:", e)

# Close the WebDriver
driver.quit()

"""
"""
QUESTION  8
------------
URL : http://adactinhotelapp.com/

NOTE: Print the UserName and Password that you are entered.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Adactin Hotel App URL
driver.get("http://adactinhotelapp.com/")

# Locate the username and password fields
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Input username and password
username_field.send_keys("TestUser123")
password_field.send_keys("TestPassword456")

# Retrieve and print the entered values
username_value = username_field.get_attribute("value")
password_value = password_field.get_attribute("value")

print("Entered Username:", username_value)
print("Entered Password:", password_value)

# Close the WebDriver
driver.quit()

"""
"""

QUESTION 9
-----------
URL : https://www.snapdeal.com/ 

NOTE: Search any product and click 1st product

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Snapdeal URL
driver.get("https://www.snapdeal.com/")

# Search for a product (e.g., "laptop")
search_box = driver.find_element(By.ID, "inputValEnter")
search_box.send_keys("laptop")  # Enter the product name
search_box.send_keys(Keys.RETURN)  # Press Enter to search

# Wait for search results to load
time.sleep(3)

# Click the first product in the search results
try:
    first_product = driver.find_element(By.XPATH, "(//div[contains(@class, 'product-tuple-image')])[1]/a")  # XPath for the first product
    first_product.click()
    print("Successfully clicked the first product.")
except Exception as e:
    print("Error clicking the first product:", e)

# Close the WebDriver
driver.quit()

"""
"""
QUESTION 10
-----------
URL : https://www.flipkart.com/ 

NOTE: Search any product and click 1st product

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Flipkart URL
driver.get("https://www.flipkart.com/")

# Close the login popup (if it appears)
try:
    close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_popup.click()
    print("Login popup closed.")
except Exception as e:
    print("Login popup not found or already closed.")

# Locate the search bar and enter a product (e.g., "mobile")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("mobile")  # Enter the product name
search_box.send_keys(Keys.RETURN)  # Press Enter to search

# Wait for search results to load
time.sleep(3)

# Click the first product in the search results
try:
    first_product = driver.find_element(By.XPATH, "(//div[contains(@class, '_1AtVbE') and .//a[contains(@class, '_1fQZEK')]])[1]//a")
    first_product.click()
    print("Successfully clicked the first product.")
except Exception as e:
    print("Error clicking the first product:", e)

# Close the WebDriver
driver.quit()

xxxxxxxxxxxxxxxxxxxxx"""

"""

QUESTION 11
-----------
URL : https://www.flipkart.com/ 

NOTE: Click login and enter User name password
      Print the details you are given.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Flipkart URL
driver.get("https://www.flipkart.com/")

# Wait for the page to load
time.sleep(2)

# Locate the username and password fields in the login popup
try:
    # Enter the username
    username_field = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    username_field.send_keys("test_user@gmail.com")
    
    # Enter the password
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys("test_password123")
    
    # Retrieve and print the entered values
    username_value = username_field.get_attribute("value")
    password_value = password_field.get_attribute("value")
    
    print("Entered Username:", username_value)
    print("Entered Password:", password_value)
except Exception as e:
    print("Error locating login fields or entering data:", e)

# Close the WebDriver
driver.quit()

xxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 12
-----------
URL : https://www.shopclues.com/wholesale.html 

NOTE: Search any product and click 1st product

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the ShopClues URL
driver.get("https://www.shopclues.com/wholesale.html")

# Locate the search bar and enter a product (e.g., "shoes")
search_box = driver.find_element(By.ID, "autocomplete")
search_box.send_keys("shoes")  # Enter the product name
search_box.send_keys(Keys.RETURN)  # Press Enter to search

# Wait for the search results to load
time.sleep(3)

# Click the first product in the search results
try:
    first_product = driver.find_element(By.XPATH, "(//div[contains(@class, 'column')])[1]//a")  # XPath for the first product
    first_product.click()
    print("Successfully clicked the first product.")
except Exception as e:
    print("Error clicking the first product:", e)

# Close the WebDriver
driver.quit()

"""
