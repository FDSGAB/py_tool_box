
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import logging


class Browser:

    def __init__(self):
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--incognito")
        #options.add_argument('--disable-gpu')
        #options.add_argument("--verbose")
        #options.add_argument("headless")
        #self.driver = webdriver.Chrome(options = options, executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options = options, executable_path = "D:\REP_programas_Python\py_tool_box\web_drivers\chromedriver.exe")

    def __repr__(self):
        return "Chrome browser that connects to the internet in the background and does not display messages in the console"
