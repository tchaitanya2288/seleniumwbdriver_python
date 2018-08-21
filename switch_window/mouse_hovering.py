from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

class Mouse_hover():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0,900);")
        time.sleep(3)
        element = driver.find_element(By.ID, "mousehover")
        itemtoclickloctor = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        # itemtoclickloctor = ".//div[@class='mouse-hover-content']//a[text()='Reload']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse hovered on element")
            time.sleep(3)
            toplink = driver.find_element(By.XPATH, itemtoclickloctor)
            actions.move_to_element(toplink).click().perform()


            print("ITEM clicked")
        except:
            print("Mouse hover failed on element")

ff = Mouse_hover()
ff.test()