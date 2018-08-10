from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class CalenderSelection():

    def test1(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        baseurl = "http://www.expedia.com"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)
        #Click flight tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        #Find departing field
        departingfield = driver.find_element_by_id("flight-departing-hp-flight")
        #click departing field
        departingfield.click()
        #Find the date to select
        dateToSelect = driver.find_element(By.CSS_SELECTOR,".datepicker-cal .datepicker-cal-month:nth-child(4) tr:nth-of-type(5) .notranslate:nth-of-type(6) [type]")
        dateToSelect.click()
        time.sleep(3)
        driver.quit()

    def test2(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        baseurl = "http://www.expedia.com"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)
        # Click flight tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Find departing field
        driver.find_element_by_id("flight-departing-hp-flight").click()
        calMonth= driver.find_element(By.XPATH,"//*[@id='flight-departing-wrapper-hp-flight']/div/div/div[2]/table/tbody/tr[5]/td[6]")
        allvalidDates = calMonth.find_elements(By.TAG_NAME, "button")

        time.sleep(5)

        for date in allvalidDates:

            if date.text == "31":
                date.click()
                break




cb = CalenderSelection()
cb.test2()
