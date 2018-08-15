from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class JavascriptExecution():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        # baseUrl = "https://letskodeit.teachable.com/"
        # driver.get(baseUrl)
        # driver = webdriver.Firefox()
        driver.maximize_window()
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")
        driver.implicitly_wait(3)


ff = JavascriptExecution()
ff.test()
