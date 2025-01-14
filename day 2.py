"""
DAY2
--------
Locators

sendKeys

"""

"""
What are the locators available in Selenium?

    ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, CSS Selector, XPath.

Which locator is faster in Selenium?

    ID.

How will you find the locators in Selenium? Write a code for it.

    WebElement element = driver.findElement(By.id("element_id"));

Explain about findElement & findElements.

    findElement locates a single element; findElements locates multiple elements.

Difference between findElement and findElements.

    findElement returns a single WebElement; findElements returns a List of WebElements.

What is the return type of findElement and findElements?

    findElement: WebElement, findElements: List<WebElement>.

In which class are all the locator methods available?

    By class.

What is the method to insert a value in a textbox?

    sendKeys().

Write a code for inserting a value in a textbox.

    driver.findElement(By.id("textbox_id")).sendKeys("value");

While finding the locators, will the index start from 0 or 1?

    0.

How will you click a button on webpages?

    driver.findElement(By.id("button_id")).click();

Is WebElement an interface or class?

    Interface.

"""
"""
QUESTION 1
----------
URL : https://www.facebook.com/ 

NOTE: Enter Email or Phone and Password.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.facebook.com/")

username = driver.find_element(By.ID,"email")
username.send_keys("mahendran@gmail.com")

password = driver.find_element(By.ID,"pass")
password.send_keys(123456)

btn = driver.find_element(By.NAME,"login")
btn.click()

"""

"""
QUESTION 2
----------
URL : https://www.redbus.in/ 

NOTE: Enter from and to textbox.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.redbus.in/ ")

from_= driver.find_element(By.ID,"src")
from_.send_keys("Erode")
from_.send_keys(Keys.ENTER)

to_= driver.find_element(By.ID,"dest")
to_.send_keys("Chennai")

"""
"""
QUESTION 3
----------
URL : https://www.google.com/

NOTE: Enter GreensTechnology. 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.google.com/")

search = driver.find_element(By.ID,"APjFqb")
search.send_keys("Greens Technology")
search.send_keys(Keys.ENTER) 

"""
"""
QUESTION 4
----------
URL : https://infinity.icicibank.com/corp/Login.jsp

NOTE: Enter username and password. 

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://infinity.icicibank.com/corp/Login.jsp")

user = driver.find_element(By.NAME,"DUMMY1")
user.send_keys("Mahendran")

driver.find_element(By.ID,"user-id-goahead").click()

driver.find_element(By.ID,"AuthenticationFG.USER_PRINCIPAL").send_keys("Mahendran")

driver.find_element(By.ID,"AuthenticationFG.ACCESS_CODE").send_keys("009876")

"""

"""
QUESTION 5
----------
URL : https://netbanking.hdfcbank.com/ 

NOTE: Enter customer id .

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()

driver.get("https://netbanking.hdfcbank.com/")

id = webdriver.find_emelentby(By.NAME,"fldLoginUserId")
id.send_keys(987654)

time.sleep(10)

"""
QUESTION 6
----------
URL : https://www.swiggy.com/

NOTE: Enter the location.

"""

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# driver.get("https://www.swiggy.com/")

# driver.find_element(By.XPATH,"//div[@role='button']").click()
# l = driver.find_element(By.XPATH,"//input[@name='']")
# l.send_keys("coimbatore")
# l.click()

"""
QUESTION 7
----------
URL :https://www.snapdeal.com/login

NOTE: Enter mobile number/email.

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# driver.get("https://www.snapdeal.com/login")

# d = driver.find_element(By.ID,"userName")
# d.send_keys(9876543210)

# btn = driver.find_element(By.ID,"checkUser")
# btn.click()

"""
QUESTION 8
-----------
URL : https://www.instagram.com/accounts/login/?hl=en login page 

NOTE: Enter username and password.

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Firefox()

# driver.get("https://www.instagram.com/accounts/login/?hl=en")

# time.sleep(10)

# u = driver.find_element(By.XPATH,"//input[@name='username']")
# u.send_keys("Mahendran")

# p = driver.find_element(By.XPATH,"//input[@name='password']")
# p.send_keys("Mahe")




"""
QUESTION 9
-----------
URL : http://demo.automationtesting.in/Register.html

NOTE: Just enter the values for the textbox only.

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# driver.get("http://demo.automationtesting.in/Register.html")

# f_name = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
# f_name.send_keys("Mahendra")

# driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Kumar")
# driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("Erode, Tamilnadu")
# driver.find_element(By.XPATH,"//input[@type='email']").send_keys("abcd@gmail.com")
# driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("9876543210")
# driver.find_element(By.XPATH,"//input[@type='password']").send_keys(9876)
# driver.find_element(By.XPATH,"//input[@ng-model='CPassword']").send_keys(9876)


"""
QUESTION 10
-----------
URL : http://adactinhotelapp.com/

NOTE: Enter Email or Phone and Password.

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# driver.get("http://adactinhotelapp.com/")

# driver.find_element(By.ID,"username").send_keys("MahendraN")
# driver.find_element(By.ID,"password").send_keys("Mahendra")




