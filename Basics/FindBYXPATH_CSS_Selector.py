from selenium import webdriver
import os


class FindelementByXPATH_CSS():

    def test(self):
        driverlocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseUrl)

        elementByXpath = driver.find_element_by_xpath("//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found element By XPath")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS is not None:
            print("We found element By Css_Selector")


CT = FindelementByXPATH_CSS()
CT.test()
