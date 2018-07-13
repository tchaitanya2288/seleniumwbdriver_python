from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class ByDemo():
    # def test(self):

    driverlocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverlocation
    driver = webdriver.Chrome(driverlocation)
    baseUrl = "https://letskodeit.teachable.com/p/practice"
    driver.get(baseUrl)


    elementById = driver.find_element(By.ID,"name")

    if elementById is not None:
        print("We found element By Id")

        elementByXpath = driver.find_element(By.XPATH,"//input[@id='displayed-text']")

    if elementByXpath is not None:
        print("We found element By Xpath")

        elementByLinkTxt = driver.find_element(By.LINK_TEXT,"Login")

    if elementByLinkTxt is not None:
        print("We found element by LinkText")

# CB = ByDemo()
# CB.test()

