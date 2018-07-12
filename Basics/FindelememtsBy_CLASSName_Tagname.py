from selenium import webdriver
import os


class FindelementByCLASSName_TAGName():

    # def test(self):
        driverlocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseUrl)

        elementByClassname = driver.find_element_by_class_name('displayed-class')
        elementByClassname.send_keys("Testing The element")

        if elementByClassname is not None:
            print("We found element By Classname")

        elementByTagname = driver.find_element_by_tag_name("a")

        if elementByTagname is not None:
            print("We found element By Tag name")


# CT = FindelementByCLASSName_TAGName()
# CT.test()
