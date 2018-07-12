from selenium import webdriver
import os

class FindByIdName():

    def test(self):

        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseUrl = "https://letskodeit.teachable.com/p/practice"

        driver.get(baseUrl)
        elementByid = driver.find_element_by_id('name')

        if elementByid is not None:
            print("We found elememt by id")

        elementByName = driver.find_element_by_class_name('btn-style')

        if elementByName is not None:
            print("We found elemnet by class name")

ct = FindByIdName()
ct.test()


