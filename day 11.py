"""
What is meant by a webtable?

    A webtable is an HTML element used to display tabular data on a webpage using <table>, <tr>, <th>, and <td> tags.

What is the use of a webtable?

    Webtables are used to organize and display structured data in rows and columns, making it easier to interpret.

Under which tags is a webtable present in HTML?

    A webtable is present under <table>, <tr>, <th>, and <td> tags in HTML.

Which tag is used to mention the table row and table data?

    The <tr> tag is used for table rows, and the <td> tag is used for table data.

Write a code to display all the column names from the table?

    columns = driver.find_elements(By.XPATH, "//table//th")
    for column in columns: print(column.text)

Write a code to display all the data from the table?

    rows = driver.find_elements(By.XPATH, "//table//tr")
    for row in rows: 
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells: print(cell.text)

If there are multiple tables available on a webpage, how will you display any specified particular webtable's data?

    Use driver.find_elements(By.XPATH, "//table")[index] to select a specific table by its index.

Write a code to print the rows alone from the webtable?

    rows = driver.find_elements(By.XPATH, "//table//tr")
    for row in rows: print(row.text)

Write a code to print all the data from the webtable using an enhanced for loop?

    rows = driver.find_elements(By.XPATH, "//table//tr")
    for row in rows: 
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells: print(cell.text)

Write a code to print the table headers from the webtable?

    headers = driver.find_elements(By.XPATH, "//table//th")
    for header in headers: print(header.text)

"""
"""
QUESTION 1
----------
URL : http://demo.guru99.com/test/write-xpath-table.html

NOTE: Print all the content in the dymaic webtable.

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demo.guru99.com/test/write-xpath-table.html")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the dynamic table rows
    rows = driver.find_elements(By.XPATH, "//table[@class='dataTable']//tr")

    # Loop through each row and print the content of each cell
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text, end=" | ")
        print()  # Move to the next line for the next row

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 2
----------
URL : http://demo.guru99.com/test/write-xpath-table.html

NOTE: Print all value in first row

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demo.guru99.com/test/write-xpath-table.html")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the first row in the table
    first_row = driver.find_elements(By.XPATH, "//table[@class='dataTable']//tr")[1]  # 1st row after the header

    # Get all the cells in the first row and print their text
    cells = first_row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text, end=" | ")
    print()  # To add a newline after printing the first row

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 3
----------
URL : http://demo.guru99.com/test/write-xpath-table.html

NOTE: Find out Number of rows available in webPage

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demo.guru99.com/test/write-xpath-table.html")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the rows in the table
    rows = driver.find_elements(By.XPATH, "//table[@class='dataTable']//tr")

    # Print the number of rows (excluding the header row)
    print("Number of rows in the table:", len(rows) - 1)  # Subtract 1 to exclude the header row

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 4
----------
URL : http://demo.guru99.com/test/write-xpath-table.html

NOTE: Print all details available in 4th webtable

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demo.guru99.com/test/write-xpath-table.html")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the 4th table on the page
    table = driver.find_elements(By.XPATH, "//table[@class='dataTable']")[3]  # 4th table (index 3)

    # Get all the rows in the 4th table
    rows = table.find_elements(By.XPATH, ".//tr")

    # Loop through each row and print the content of each cell
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text, end=" | ")
        print()  # Move to the next line for the next row

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

"""
QUESTION 5
----------
URL : http://demo.guru99.com/test/write-xpath-table.html

NOTE: Print Even rows  available in 4th webtable

"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (use the path to your driver)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("http://demo.guru99.com/test/write-xpath-table.html")
    driver.maximize_window()
    time.sleep(2)  # Allow the page to load

    # Locate the 4th table on the page
    table = driver.find_elements(By.XPATH, "//table[@class='dataTable']")[3]  # 4th table (index 3)

    # Get all the rows in the 4th table
    rows = table.find_elements(By.XPATH, ".//tr")

    # Loop through each row and print even rows (index 1, 3, 5, etc.)
    for index, row in enumerate(rows):
        if index % 2 != 0:  # Even rows have odd index (1-based counting)
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                print(cell.text, end=" | ")
            print()  # Move to the next line for the next row

finally:
    # Close the browser
    driver.quit()
xxxxxxxxxxxxxxxxxxxxxxxxx"""
