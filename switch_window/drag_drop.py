from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
import time

class DragAndDrop():
    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        baseUrl = "https://jqueryui.com/droppable/"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        fromelement = driver.find_element(By.ID, "draggable")
        toelement   = driver.find_element(By.ID, "droppable")
        time.sleep(3)
        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(fromelement,toelement).perform()
            actions.click_and_hold(fromelement).move_to_element(toelement).release().perform()
            print("drag drop element successful")
            time.sleep(2)
        except:
            print("drag and drop on element failed")

ff = DragAndDrop()
ff.test()
