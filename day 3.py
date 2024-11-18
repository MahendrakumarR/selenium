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
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")

time.sleep(2)


search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("iPhone").click()
time.sleep(2)

"""
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
    if language.text == "Tamil":
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

