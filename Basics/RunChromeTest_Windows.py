from selenium import webdriver
import os

class RunchromeTest_windows():

    def test(self):

        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.letskodeit.com")

CT = RunchromeTest_windows()
CT.test()
