from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class Scrolling_element():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)
        #Scroll down
        driver.execute_script("window.scrollBy(0,1300);")
        time.sleep(3)
        #Scroll Up
        driver.execute_script("window.scrollBy(0,-1300);")
        time.sleep(3)
        #Scroll element into view
        element = driver.find_element(By.ID,"mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150);")
        #Native way to scrollelement into view
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-1300);")
        location = element.location_once_scrolled_into_view
        print("Location : ", str(location))

ff = Scrolling_element()
ff.test()
