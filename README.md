# selenium-python

import unittest
from time import sleep

from selenium import webdriver


class TestParallel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wb/hub",
                                       desired_capabilities={"browserName": "chrome",
                                                             })
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def method1(self):
        self.driver.get("https://www.google.com/")
        sleep(2)

    def method2(self):
        self.driver.get("https://www.apple.com/")
        sleep(2)

    def method3(self):
        self.driver.get("https://www.twitter.com/")
        sleep(2)

    def method4(self):
        self.driver.get("https://www.facebook.com/")
        sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

