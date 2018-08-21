from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class Switch_To_frame():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)
        driver.find_element(By.ID, "name").send_keys("Chaitanya")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        driver.find_element(By.ID, "name").send_keys("Chaitanya")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()

ff = Switch_To_frame()
ff.test()

