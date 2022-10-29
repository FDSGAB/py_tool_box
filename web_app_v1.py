import browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#https://www.geeksforgeeks.org/working-with-input-box-test-box-in-selenium-with-python/
#https://selenium-python.readthedocs.io/locating-elements.html

class WebApp:

    user = "BLABLABLA"
    password = "123456"
    phone_no = "4093432940"

    def __init__(self):
        chrome = browser.Browser()
        chrome.driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        element = chrome.driver.find_elements(By.CLASS_NAME, "text_field")
        chrome.driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-1"]').send_keys(self.user)
        chrome.driver.find_element(By.XPATH,'//*[@id="RESULT_TextField-2"]').send_keys(self.password)
        chrome.driver.find_element(By.XPATH,'//*[@id="RESULT_TextField-3"]').send_keys(self.phone_no)
        time.sleep(10)
        #chrome.driver.find_elements(By.NAME, 'Submit')[0].send_keys(Keys.ENTER)
        chrome.driver.find_element(By.XPATH,'//*[@id="FSsubmit"]').send_keys(Keys.ENTER)
        time.sleep(5)
        print(browser.Browser())
        chrome.driver.close()


WebApp()
