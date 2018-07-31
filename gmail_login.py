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
        time.sleep(5)
        logout1 = browser.find_element_by_css_selector(".gb_8a")
        logout1.click()
        time.sleep(10)
        logout2 = browser.find_element_by_css_selector(".gb_6f")
        logout2.click()
        # signout_Button = browser.find_element_by_xpath("/html//div[@id='gb']/div[1]/div[1]/div/div[5]/div[2]//a[@href='https://accounts.google.com/Logout?hl=en&continue=https://mail.google.com/mail&service=mail&timeStmp=1533066955&secTok=.AG5fkS89eexWEFgKfL8iwtRRZ4GEjHBZpg']")
        # signout_Button.click()
        time.sleep(4)


print("python script executed")

GL = gmail_login()
GL.gmail_test()
