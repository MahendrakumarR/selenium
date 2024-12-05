from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Firefox()  # Ensure chromedriver is in PATH or specify its location
driver.maximize_window()

# Open the URL
driver.get("http://demo.guru99.com/test/drag_drop.html")

# Wait for the page to load
time.sleep(2)

# Locate the draggable elements
bank_element = driver.find_element(By.XPATH, "//li[@id='credit2']")
amount_5000 = driver.find_element(By.XPATH, "//li[@id='fourth']")

# Locate the droppable areas
debit_account = driver.find_element(By.XPATH, "//ol[@id='bank']")
debit_amount = driver.find_element(By.XPATH, "//ol[@id='amt7']")


# Perform drag-and-drop actions
actions = ActionChains(driver)
actions.drag_and_drop(bank_element, debit_account).perform()
actions.drag_and_drop(amount_5000, debit_amount).perform()


# Pause to observe results
time.sleep(5)

