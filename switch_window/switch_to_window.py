from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class SwitchToWindow():

    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)
        #Find parent handle --> Main window
        parenthandle = driver.current_window_handle
        print("Parent Handle:", parenthandle)
        #find openwindow button and click it
        driver.find_element(By.ID,"openwindow").click()
        time.sleep(3)
        #Find all handles there should two handles after clicking open window
        handles = driver.window_handles
        #switch to handle and search course
        for handle in handles:
            print("Hanlde:", handle)
            if handle not in parenthandle:
                driver.switch_to.window(handle)
                print("switch to window::", handle)
                searchbox = driver.find_element(By.ID, "search-courses")
                searchbox.send_keys("python")
                time.sleep(2)
                driver.close()
                break
        driver.switch_to.window(parenthandle)
        driver.find_element(By.ID, "name").send_keys("Test Sucessful")


ff = SwitchToWindow()
ff.test()



