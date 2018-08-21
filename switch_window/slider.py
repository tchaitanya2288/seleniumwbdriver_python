from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
import time

class Sliders():
    def test1(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        baseUrl = "https://jqueryui.com/slider/"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']/span")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element,200,0).perform()
            time.sleep(2)
            print("Slider element performed successful")

        except:
            print("element failed on slider")



ff = Sliders()
ff.test1()
