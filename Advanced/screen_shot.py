from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class Screenshots():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseUrl = "https://letskodeit.teachable.com/"
        driver.get(baseUrl)
        # driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abcde")
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = "C:\\Users\\Chaithanya\\Desktop\\test.png" # Mac
        # destinationFileName = "C:\\atomar\\Desktop" -> Windows

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: ", destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()