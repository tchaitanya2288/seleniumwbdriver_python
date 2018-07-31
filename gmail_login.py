from selenium import webdriver
import os
import time

class gmail_login():
    def gmail_test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        browser = webdriver.Chrome(driverLocation)
        browser.get('http://gmail.com')

        emailElem = browser.find_element_by_name('identifier')
        emailElem.send_keys('tchaitanya.2288@gmail.com')
        nextButton = browser.find_element_by_xpath("//div[@id='identifierNext']/content[@class='CwaK9']")
        nextButton.click()
        time.sleep(4)
        passwordElem = browser.find_element_by_name('password')
        passwordElem.send_keys('chaitupraveen')
        signButton = browser.find_element_by_xpath("//div[@id='passwordNext']/content[@class='CwaK9']")
        signButton.click()
        time.sleep(4)
        browser.quit()


GL = gmail_login()
GL.gmail_test()