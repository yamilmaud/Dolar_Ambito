# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import time


class Crawler:
    def __init__(self, browser, headless):
        self.browser = browser
        self.headless = headless


    def create_driver(self):
        #
        # options = Options()
        # options.headless = self.headless

        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=r"C:\Users\Souls\Desktop\chromedriver_win32\chromedriver.exe")
        else:
            driver = webdriver.Firefox(executable_path=r"C:\Users\Souls\Desktop\chromedriver_win32\geckodriver.exe")
        return driver



    def crawl(self, driver, url):
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)




# if __name__ == '__main__':
#     CrawlerWeb(HOME_URL)
