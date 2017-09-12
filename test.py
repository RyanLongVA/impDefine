#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
    driver.get('https://hackerone.com/yahoo')
print driver.page_source

#if __name__ == '__main__':

