from selenium import webdriver
import time
import os

class window_size():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/")
        driver.implicitly_wait(3)
        height = driver.execute_script("return window.innerHeight")
        width = driver.execute_script("return window.innerWidth")
        print("Height :", str(height))
        print("Width :", str(width))
        driver.quit()

ff = window_size()
ff.test()