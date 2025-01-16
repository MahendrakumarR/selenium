# Locator(xpath)
# Radio button,checkbox, Button

""" 
What are the different types of XPath?
    
    The types of XPath are Absolute XPath and Relative XPath.

What is XPath? Why do we use XPath?
    
    XPath is a query language for selecting nodes in XML documents; it's used in Selenium to locate elements precisely within HTML.

What are the Types of XPath? 
    
    There are two main types: Absolute XPath (starting from root) and Relative XPath (starting from any node).

What is the difference between Absolute XPath and Relative XPath?

    Absolute XPath begins from the root element (/html), while Relative XPath starts from a chosen node (//node).

What is the difference between / and // in XPath?

    / selects from the root node, while // selects nodes from anywhere in the document.

What is the difference between a Radio Button and a Checkbox?
    
    A Radio Button allows a single selection, while a Checkbox allows multiple selections.

What is the method used to perform a click?

    The .click() method is used to simulate a click action.

What are the XPath functions?
    
    Common functions include text(), contains(), starts-with(), and last().

How will you select a female Radio Button and write a code for it?

    driver.find_element_by_xpath("//input[@value='female']").click()

Write a code for selecting a Radio Button and Checkbox button click?

    driver.find_element_by_xpath("//input[@type='radio']").click()

    driver.find_element_by_xpath("//input[@type='checkbox']").click()

What are the methods available in XPath?
    
    XPath methods include find_element_by_xpath(), find_elements_by_xpath(), and various XPath functions like contains(), starts-with(), and text().


"""
"""
QUESTION 1
-----------
URL : https://www.amazon.in/

NOTE: Click start here. Enter iphone and search

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")

time.sleep(2)


search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("iPhone")
search_box.click()

time.sleep(2)



"""
QUESTION 2
-----------
URL : https://www.facebook.com/

NOTE: Enter email and password and click login(by using xpath locator).

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.facebook.com/")

time.sleep(3)

email = driver.find_element(By.XPATH,"//input[@placeholder='Email address or phone number']")
email.send_keys("mahendra@gmail.com")

password = driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys("mahendra@g")

time.sleep(2)

button = driver.find_element(By.XPATH,"//button[@name='login']")
button.click()
"""


"""
QUESTION 3
-----------
URL : http://demo.automationtesting.in/Register.html

NOTE: Give details and register the form.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("http://demo.automationtesting.in/Register.html")

time.sleep(3)

f_name = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
f_name.send_keys("MahendraN")

l_name = driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")
l_name.send_keys("R")

a_name = driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']")
a_name.send_keys("Erode")

e_name = driver.find_element(By.XPATH,"//input[@type='email']")
e_name.send_keys("ahendra@gmail.com")

t_name = driver.find_element(By.XPATH,"//input[@type='tel']")
t_name.send_keys("0987654321")

g_name = driver.find_element(By.XPATH,"//input[@value='Male']")
g_name.click()

c_name = driver.find_element(By.XPATH,"//input[@value='Cricket']")
c_name.click()

m_name = driver.find_element(By.XPATH,"//input[@value='Movies']")
m_name.click()

la_name = driver.find_element(By.ID,"msdd")
la_name.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class,'ui-autocomplete')]/li/a")))

languages = driver.find_elements(By.XPATH, "//ul[contains(@class,'ui-autocomplete')]/li/a")
for language in languages:
    if language.text == "English":
        language.click()
        break 

time.sleep(2)

driver.find_element(By.XPATH, "//label[text()='Languages']").click()

s_name = Select(driver.find_element(By.ID,"Skill"))
s_name.select_by_visible_text('APIS')


c_name = Select(driver.find_element(By.ID,"countries"))
c_name.select_by_visible_text("india")


y_name = Select(driver.find_element(By.XPATH,"//input[@placeholder='Year']"))
y_name.select_by_value("2000") 

m_name = Select(driver.find_element(By.XPATH,"//input[@placeholder='Month']"))
m_name.select_by_visible_text("May")

d_name = Select(driver.find_element(By.XPATH,"//input[@placeholder='Day']"))
d_name.select_by_value("10")

p_name = driver.find_element(By.ID,"firstpassword")
p_name.send_keys("MahendraN")

cp_name = driver.find_element(By.ID,"secondpassword")
cp_name.send_keys("MahendraN")

time.sleep(3)

btn = driver.find_element(By.ID,"submitbtn")
btn.click()

time.sleep(3)

""" """===== Not Completed """
"""

QUESTION 4
-----------
URL : http://demoqa.com/automation-practice-form/

NOTE: Give details and register the form

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()

driver.get("http://demoqa.com/automation-practice-form/")

driver.find_element(By.ID, "firstName").send_keys("MahendraN")

driver.find_element(By.ID, "lastName").send_keys("R")

driver.find_element(By.ID, "userEmail").send_keys("Mahendra@gmail.com")

driver.find_element(By.XPATH, "//label[text()='Male']").click()

driver.find_element(By.ID, "userNumber").send_keys("987654320") 

driver.find_element(By.ID, "dateOfBirthInput").click()
Select(driver.find_element(By.CLASS_NAME,"react-datepicker__year-select")).select_by_visible_text("2000")
Select(driver.find_element(By.CLASS_NAME,"react-datepicker__month-select")).select_by_visible_text("June")
# driver.find_element(By.XPATH,"//div[text()='15']").click()
driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15' and not(contains(@class, 'outside-month'))]").click()

driver.find_element(By.ID,"subjectsInput").send_keys("Maths")
time.sleep(1)
driver.find_element(By.ID,"subjectsInput").send_keys('\n')

driver.find_element(By.XPATH,"//label[text()='Sports']").click()
driver.find_element(By.XPATH,"//label[text()='Music']").click()

upload_element = driver.find_element(By.ID,"uploadPicture")
upload_element.send_keys("C:/Users/Administrator/Downloads/qwert.JPEG")

driver.find_element(By.ID,"currentAddress").send_keys("123, jhon street, chennai,chennai 001")

driver.find_element(By.ID,"state").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[text()='NCR']").click()

driver.find_element(By.ID, "city").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

driver.find_element(By.ID,"submit").click()

time.sleep(5)

""" """===== Not Completed """

"""
QUESTION 5
----------
URL : http://www.greenstechnologys.com/

NOTE: Print the paragraph starts with Greens Technology
"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()

driver.get("http://www.greenstechnologys.com/")

pragraph = driver.find_elements(By.TAG_NAME,'p')

for para in pragraph:
    if para.text.startswith("Greens Technology"):
        print(para.text)
        break
"""
"""
QUESTION 5
-----------
URL : http://greenstech.in/selenium-course-content.html

NOTE: Click interview question +.
      Click cts  interview question

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (make sure to download and specify the correct driver for your browser)
driver = webdriver.Firefox()

try:
    # Open the URL
    driver.get("http://greenstech.in/selenium-course-content.html")
    
    # Maximize the browser window
    driver.maximize_window()
    
    # Wait for the page to load
    time.sleep(2)
    
    # Click on "Interview Question +" to expand the section
    interview_question_plus = driver.find_element(By.XPATH, "//h2[contains(text(),'Interview Questions')]")
    interview_question_plus.click()
    
    # Wait for the options to load
    time.sleep(2)
    
    # Click on "CTS Interview Question"
    cts_question = driver.find_element(By.XPATH, "//a[contains(text(),'CTS Interview Question')]")
    cts_question.click()
    
    # Wait to observe the action (optional)
    time.sleep(5)
    
finally:
    # Close the browser
    driver.quit()

"""

"""

QUESTION 6
----------
URL : https://www.redbus.in/

NOTE: Click ^[opposite of this] and  signin/signup 
      Enter Mobilenumber and click Generate OTP

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open the Redbus website
driver.get("https://www.redbus.in/")

# Maximize the window
driver.maximize_window()

# Wait for the page to load completely
time.sleep(5)

# Click on the Sign-in/Sign-up button (^) opposite of this
signin_button = driver.find_element(By.ID, "i-icon-profile")
signin_button.click()

time.sleep(2)  # Wait for the dropdown to appear

# Select the "Sign In/Sign Up" option
sign_in_option = driver.find_element(By.ID, "signInLink")
sign_in_option.click()

# Wait for the modal to appear
time.sleep(5)

# Switch to the iframe where the mobile number input is present
iframe = driver.find_element(By.XPATH, "//iframe[contains(@class, 'modalIframe')]")
driver.switch_to.frame(iframe)

# Enter the mobile number
mobile_input = driver.find_element(By.XPATH, "//input[@id='mobileNoInp']")
mobile_input.send_keys("9876543210")  # Replace with the mobile number you want to use

# Click on the Generate OTP button
generate_otp_button = driver.find_element(By.XPATH, "//button[contains(text(), 'GENERATE OTP')]")
generate_otp_button.click()

# Wait for the OTP page to load
time.sleep(5)

# Exit the iframe to switch back to the main content
driver.switch_to.default_content()

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx """

"""
QUESTION 7
----------
URL : https://www.cleartrip.com/trains

NOTE: Enter From ,TO  and click search trains

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open the Cleartrip Trains website
driver.get("https://www.cleartrip.com/trains")
driver.maximize_window()

# Wait for the page to load completely
time.sleep(5)

# Print the page source to verify element presence
print(driver.page_source)  # To see if the "to_station" element exists

# Enter the "From" station
from_input = driver.find_element(By.ID, "from_station")
from_input.clear()
from_input.send_keys("Chennai")  # Replace with your desired 'From' location
time.sleep(2)  # Wait for auto-suggestions to load
from_input.send_keys(Keys.DOWN)  # Select the first suggestion
from_input.send_keys(Keys.RETURN)

# Wait for suggestions and field completion
time.sleep(3)

# Try to find the "To" station input
try:
    to_input = driver.find_element(By.ID, "to_station")
    to_input.clear()
    to_input.send_keys("Bangalore")  # Replace with your desired 'To' location
    time.sleep(2)  # Wait for auto-suggestions to load
    to_input.send_keys(Keys.DOWN)  # Select the first suggestion
    to_input.send_keys(Keys.RETURN)
except Exception as e:
    print(f"Error: {e}")
    print("Element 'to_station' not found.")

# Wait for the fields to be fully populated before clicking the search button
time.sleep(3)

# Click on the "Search Trains" button
try:
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search trains')]")
    search_button.click()
except Exception as e:
    print(f"Error: {e}")
    print("Search button not found.")

# Wait for the results page to load
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

""" 
QUESTION 8
-----------
URL :http://greenstech.in/selenium-course-content.html

NOTE: Click Model Reume + and click Resume Model 1

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Firefox()  # Replace with the appropriate driver for your browser

# Open the Greenstech website
driver.get("http://greenstech.in/selenium-course-content.html")
driver.maximize_window()

# Wait for the page to load completely
time.sleep(5)

# Use WebDriverWait to wait for the "Model Resume +" button to be clickable
try:
    model_resume_plus_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Model Resume +')]"))
    )
    model_resume_plus_button.click()
    print("Clicked 'Model Resume +' button.")
except Exception as e:
    print(f"Error: {e}")

# Wait for the dropdown or modal to load
time.sleep(2)

# Click on "Resume Model 1" button with improved XPath
try:
    resume_model_1_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Resume Model 1')]"))
    )
    resume_model_1_button.click()
    print("Clicked 'Resume Model 1' button.")
except Exception as e:
    print(f"Error: {e}")

# Wait for the page to load or interact
time.sleep(5)

# Close the browser
driver.quit()

xxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 9
-----------
URL : https://www.flipkart.com/

NOTE: Click Login and Entere Username password 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open Flipkart website
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Close the login pop-up if it appears
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
    close_button.click()
except Exception as e:
    print(f"Error: {e} - Pop-up may not have appeared.")

# Click on the "Login" button
login_button = driver.find_element(By.XPATH, "//a[contains(@href, '/account/login')]")
login_button.click()

# Wait for the login page to load
time.sleep(3)

# Find username and password fields
username_field = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")

# Enter username and password (replace with your credentials)
username_field.send_keys("your_username_here")  # Replace with actual username
password_field.send_keys("your_password_here")  # Replace with actual password

# Click on the "Login" button to submit the form
login_submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_submit_button.click()

# Wait for login to complete
time.sleep(5)

# Close the browser
driver.quit()

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""
"""
QUESTION 10
-----------
URL : https://www.amazon.in/

NOTE: Click any  product and click search

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open Amazon website
driver.get("https://www.amazon.in/")
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Find and click on the first product from the displayed list
product = driver.find_element(By.XPATH, "//div[@class='s-main-slot']//div[@data-index='1']")
product.click()

# Wait for the product page to load
time.sleep(3)

# Now, click on the search bar and enter the product name to search
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
product_name = driver.title  # Getting the product name from the product page
search_bar.clear()
search_bar.send_keys(product_name)  # Enter the product name into the search bar
search_bar.send_keys(Keys.RETURN)  # Press Enter to search

# Wait for the search results to load
time.sleep(5)

# Close the browser
driver.quit()

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""
"""
QUESTION 11
-----------
URL : https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp

NOTE: Give details and register the form.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open Google Sign-Up page
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Fill in the details

# First Name
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("John")

# Last Name
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Doe")

# Username (email)
username = driver.find_element(By.ID, "username")
username.send_keys("john.doe12345")  # Make sure the username is available

# Password
password = driver.find_element(By.NAME, "Passwd")
password.send_keys("SecurePassword123")  # Replace with a valid password

# Confirm Password
confirm_password = driver.find_element(By.NAME, "ConfirmPasswd")
confirm_password.send_keys("SecurePassword123")  # Make sure it matches the password

# Click on the "Next" button to continue
next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
next_button.click()

# Wait for the next page to load
time.sleep(5)

# After the first page, there might be additional steps like phone verification. 
# To fully automate, those would need handling too, but this script covers the basic form submission.

# Close the browser
driver.quit()
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

"""

QUESTION 12
-----------
URL : https://www.snapdeal.com/

NOTE: Click signin and click new register and enter mobile number abd click continue.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open Snapdeal website
driver.get("https://www.snapdeal.com/")
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Click on the "Sign In" button
sign_in_button = driver.find_element(By.XPATH, "//span[text()='Sign In']")
sign_in_button.click()

# Wait for the sign-in page to load
time.sleep(3)

# Click on the "New Register" button
new_register_button = driver.find_element(By.XPATH, "//a[text()='New to Snapdeal? Register']")
new_register_button.click()

# Wait for the registration form to appear
time.sleep(3)

# Enter mobile number (replace with the desired number)
mobile_number_field = driver.find_element(By.ID, "userName")
mobile_number_field.send_keys("9876543210")  # Replace with your mobile number

# Click on the "Continue" button
continue_button = driver.find_element(By.XPATH, "//button[text()='Continue']")
continue_button.click()

# Wait for the next page to load
time.sleep(5)

# Close the browser
driver.quit()
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

"""
QUESTION 13
-----------
URL : https://www.myntra.com/register?referer=https://www.myntra.com/

NOTE: Enter Mobile number and click continue

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open Myntra registration page
driver.get("https://www.myntra.com/register?referer=https://www.myntra.com/")
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Find the mobile number input field and enter a mobile number
mobile_number_field = driver.find_element(By.XPATH, "//input[@type='tel']")
mobile_number_field.send_keys("9876543210")  # Replace with your mobile number

# Find the "Continue" button and click it
continue_button = driver.find_element(By.XPATH, "//button[text()='Continue']")
continue_button.click()

# Wait for the next page to load (if applicable)
time.sleep(5)

# Close the browser
driver.quit()
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

"""
QUESTION 14
------------
URL : https://www.swiggy.com/

NOTE: Click sign up and Give details and register the form.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

# Open Swiggy website
driver.get("https://www.swiggy.com/")
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Click on the "Sign Up" button
sign_up_button = driver.find_element(By.XPATH, "//a[text()='Sign Up']")
sign_up_button.click()

# Wait for the sign-up page to load
time.sleep(3)

# Fill in the registration form

# Name field
name_field = driver.find_element(By.NAME, "name")
name_field.send_keys("John Doe")  # Replace with your name

# Mobile Number field
mobile_field = driver.find_element(By.NAME, "mobile")
mobile_field.send_keys("9876543210")  # Replace with your mobile number

# Email field
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("johndoe@example.com")  # Replace with your email

# Password field
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SecurePassword123")  # Replace with your password

# Click on the "Sign Up" button
sign_up_submit_button = driver.find_element(By.XPATH, "//button[text()='SIGN UP']")
sign_up_submit_button.click()

# Wait for the registration process to complete
time.sleep(5)

# Close the browser
driver.quit()
XXXXXXXXXXXXXXXXXXXXXXXXXXXX"""