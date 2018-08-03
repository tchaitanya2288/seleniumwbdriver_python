from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class clickandsendkeys():
    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseUrl = "https://letskodeit.teachable.com/"
        #Winndow Maximize
        driver.maximize_window()
        #Open the URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        loginlink = driver.find_element(By.XPATH,"/html//div[@id='navbar']//ul[@class='nav navbar-nav navbar-right']//a[@href='/sign_in']")
        loginlink.click()

        emailfield = driver.find_element(By.ID,"user_email")
        emailfield.send_keys("test")

        passwordfield = driver.find_element(By.ID,"user_password")
        passwordfield.send_keys("test")

        time.sleep(3)

        emailfield.clear()
        time.sleep(5)
        emailfield.send_keys("test")
        time.sleep(5)
        driver.quit()



cc = clickandsendkeys()
cc.test()