"""
1.Introduction to selenium
2.Download jar file and drivers
3.Browser Launch

"""
"""
What is Automation Testing and benefits?

    Automation Testing involves using software tools to run tests automatically. Benefits include faster testing, higher accuracy, reusability of tests, and ease of testing complex scenarios.

Why should Selenium be selected as a test tool?
    
    Selenium is open-source, supports multiple programming languages, integrates with various frameworks, and can run tests across different browsers and operating systems.

What is Selenium? What are the different Selenium components?

    Selenium is a suite of tools for automating web browsers. Its components include:

        Selenium IDE
        Selenium RC (Remote Control)
        WebDriver
        Selenium Grid

What is the difference between Selenium IDE, Selenium RC, and WebDriver?

    Selenium IDE: A browser plugin for recording and running tests.
    Selenium RC: An older tool for executing tests using JavaScript, now deprecated.
    WebDriver: The latest tool that interacts directly with the browser, offering more control and supporting multiple programming languages.

What is the latest version of selenium jar file and how you will configure selenium jar file with eclipse?

    The latest version can be checked on the official Selenium website. To configure, download the jar file, add it to your project in Eclipse via Build Path > Configure Build Path > Libraries > Add External JARs.

Can Google Chrome be supported by Selenium IDE?

    Yes, Selenium IDE supports Google Chrome through a browser extension.

What are the different browsers supported by Selenium?

    Selenium supports Chrome, Firefox, Safari, Internet Explorer (IE), Microsoft Edge, and Opera.

What is the Classname, driver name for the below browsers:

    Firefox browser: FirefoxDriver, geckodriver
    Chrome browser: ChromeDriver, chromedriver
    IE: InternetExplorerDriver, IEDriverServer
    Safari browser: SafariDriver, safaridriver
    Opera browser: OperaDriver, operadriver

What is the WebDriver and is WebDriver a class or interface?

    WebDriver is an interface that defines methods for controlling a web browser.

What is the method name to launch the URL?

    driver.get("URL");

Method names to get the title and current URL?

    driver.getTitle(); (for title)
    driver.getCurrentUrl(); (for current URL)

What is the difference between close() and quit()? (one-line answer)

    close(): Closes the current browser window.
    quit(): Closes all browser windows and ends the WebDriver session.

"""
"""
QUESTIONS(practical)
----------------------
1.Launch the below URL's in firefox browser:
-------------------------------------------
	1.Greens technologys - http://www.greenstechnologys.com/
	2.Facebook - https://www.facebook.com/
    3.Amazon - https://www.amazon.in
	4.Greens technologys-http://greenstech.in/selenium-course-content.html

"""
# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get("http://www.greenstechnologys.com/")
# driver.get("https://www.facebook.com/")
# driver.get("https://www.amazon.in")
# driver.get("http://greenstech.in/selenium-course-content.html")

"""
2.Launch the below URL's in chrome browser:
------------------------------------------
	1.Greens technologys - http://www.greenstechnologys.com/
    2.Gmail - http://gmail.com/
	3.Flipkart - http://www.flipkart.com/
	4.Greens technology-http://greenstech.in/selenium-course-content.html

"""
# from selenium import webdriver

# driver_chrome = webdriver.Chrome()

# driver_chrome.get("http://www.greenstechnologys.com/")
# driver_chrome.get("http://gmail.com/")
# driver_chrome.get("http://www.flipkart.com/")
# driver_chrome.get("http://greenstech.in/selenium-course-content.html")

"""
3.Launch the below URL's in IE browser:
--------------------------------------
	1.Greens technologys - http://www.greenstechnologys.com/
	2.DemoQa Registration http://demo.automationtesting.in/Register.html
    3.Greens technologys- http://greenstech.in/selenium-course-content.html

"""
from selenium import webdriver

driver_ie = webdriver.Ie()

# driver_ie.get("http://www.greenstechnologys.com/")
# driver_ie.get("http://demo.automationtesting.in/Register.html")
# driver_ie.get("http://greenstech.in/selenium-course-content.html")