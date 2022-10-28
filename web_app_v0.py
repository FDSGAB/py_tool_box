import browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#https://www.geeksforgeeks.org/working-with-input-box-test-box-in-selenium-with-python/

class WebApp:

    def __init__(self):
        chrome = browser.Browser()
        chrome.driver.get("https://www.google.com/")
        inputElement = chrome.driver.find_elements(By.TAG_NAME, "input")
        inputElement[0].send_keys('あいみょん')
        inputElement[0].send_keys(Keys.ENTER)
        time.sleep(3636)
        chrome.driver.close()


WebApp()
