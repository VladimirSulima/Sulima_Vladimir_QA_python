from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome("E:\PythonProjects\SeleniumFramework\BrowserDrivers\chromedriver.exe")
        self.wait = WebDriverWait(self.instance, 15)

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

