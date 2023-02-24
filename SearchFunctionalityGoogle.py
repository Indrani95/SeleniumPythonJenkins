import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):

    def test_launch_browser(self):
        filePath = "C:\\Users\\ranje\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
        driver = webdriver.Chrome(filePath)
        time.sleep(1)
        url = "https://www.google.com/"
        driver.get(url)
        time.sleep(2)
        # Search Functionality
        enterSomething = driver.find_element(By.NAME, "q")
        enterSomething.send_keys("selenium")
        time.sleep(2)
        enterSomething.send_keys(Keys.ENTER)
        time.sleep(1)
        expectedResult = "selenium - Google Search"
        actualResult = driver.title
        time.sleep(1)
        print(actualResult)
        assert expectedResult == actualResult
        time.sleep(1)
        driver.quit()
if __name__ == '__main__':
    unittest.main()