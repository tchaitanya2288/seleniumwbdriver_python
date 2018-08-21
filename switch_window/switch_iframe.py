from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class SwitchToiframe():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0,1300);")
        #switch to frame using id
        driver.switch_to.frame("courses-iframe")
        # driver.switch_to.frame(0)
        time.sleep(2)
        #search course
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(2)
        #switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1300);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")


ff = SwitchToiframe()
ff.test()