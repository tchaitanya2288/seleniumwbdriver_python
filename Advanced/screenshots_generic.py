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
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abcde")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)

    def takeScreenshot(self, driver):

        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Users\\Chaithanya\\Desktop\\"
        DestinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(DestinationFile)
            print("Screenshot saved to directory --> :: ", DestinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()