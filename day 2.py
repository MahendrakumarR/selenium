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

