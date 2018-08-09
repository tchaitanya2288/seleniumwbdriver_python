from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class Demo_ListOfElements():
    # def test(self):

    driverlocation = "C:\\Users\\Chaithanya\\Documents\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverlocation
    driver = webdriver.Chrome(driverlocation)
    baseUrl = "https://letskodeit.teachable.com/p/practice"
    driver.get(baseUrl)


    elementslistByClassname = driver.find_elements_by_class_name("inputs")
    length1 = len(elementslistByClassname)

    if elementslistByClassname is not None:
        print("Class Name----> elements list is", str(length1))

    elementlistByTagname = driver.find_element(By.TAG_NAME,"td")
    length2 = len(elementlistByTagname)

    if elementlistByTagname is not None:
        print("Tag Name ---> Size of the list is", str(length2))



# CB = ByDemo()
# CB.test()
