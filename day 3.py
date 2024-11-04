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
try:

   start_here = driver.find_element(By.LINK_TEXT,"Start here")
   start_here.click()
   time.sleep(2)
except:
    print("Start link here not work")


search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("iPhone")
time.sleep(2)
driver.quit()