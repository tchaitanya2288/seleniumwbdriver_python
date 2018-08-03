from selenium import webdriver
import os

class BrowserInteractions():
    def test(self):
        driverLocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseUrl = "https://saveonenergy.ca/"
        #Winndow Maximize
        driver.maximize_window()
        #Open the URL
        driver.get(baseUrl)
        #Get Title
        title = driver.title
        print("The Title of the WebPage is:", str(title))
        currentUrl = driver.current_url
        print("Current URL of webpage is:", currentUrl)
        #Browser Refresh
        driver.refresh()
        print("driver Refreshed 1st time")
        driver.get(driver.current_url)
        #Browser Refresh 2nd time
        print("driver Refreshed 2nd time")
        #Open another URL
        driver.get("https://saveonenergy.ca/Consumer.aspx")
        #Browser Back
        driver.back()
        #Browser Forward
        driver.forward()
        #Browser close/quit
        #driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()


