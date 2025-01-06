
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
xxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Print paragaraph starts with vel murugan.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://greenstech.in/selenium-course-content.html")

# Locate the paragraph starting with "Vel Murugan"
paragraph = driver.find_element(By.XPATH, "//p[starts-with(text(), 'Vel Murugan')]").text

# Print the paragraph
print(paragraph)

# Close the WebDriver
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 3
----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Print the adayar branch address

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("http://greenstech.in/selenium-course-content.html")

time.sleep(10)
# Locate the Adyar branch address
try:
    address = driver.find_element(By.XPATH, "//p[contains(text(), 'Adyar')]").text
    print("Adyar Branch Address:", address)
except Exception as e:
    print("Error locating the Adyar branch address:", e)

# Close the WebDriver
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxx"""

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



