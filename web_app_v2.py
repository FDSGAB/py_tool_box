from filecmp import clear_cache
import os
from browser import Browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#https://www.geeksforgeeks.org/working-with-input-box-test-box-in-selenium-with-python/
#https://selenium-python.readthedocs.io/locating-elements.html
#https://www.softwaretestingmaterial.com/how-to-handle-web-tables-in-selenium-python/

class WebApp:

    def __init__(self):
        chrome = Browser()
        chrome.driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
        # to identify the table rows
        rows = chrome.driver.find_elements(By.XPATH, '//*[@class="spTable"]/tbody/tr')
        for e in rows:
            e.find_elements(By.XPATH,'//*[@class="spTable"]/td')
            print(e.text.split(" ")[3]) #RETURNS STRINGS
        print(len(rows))
        #time.sleep(10)
        clear_cache()
        chrome.driver.close()


WebApp()
