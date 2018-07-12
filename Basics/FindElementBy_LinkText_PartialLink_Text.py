from selenium import webdriver
import os

class FindElementBy_LinkTxt_PartialTxt():

    # def test(self):

        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseUrl = "https://www.randstad.ca/"
        driver.get(baseUrl)

        elementByLinktxt = driver.find_element_by_link_text("about")

        if elementByLinktxt is not None:
            print("We found element by link text")

        elementByPartial_Linktxt = driver.find_element_by_partial_link_text("loca")

        if elementByPartial_Linktxt is not None:
            print("We found element By Partial Link Text")


# CW = FindElementBy_LinkTxt_PartialTxt()
# CW.test()





