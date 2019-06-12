import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = "12.2",
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = '/Users/craigball/Library/Developer/Xcode/DerivedData/Buses-fqvkaypivbiteuagkyhnzqftjgtn/Build/Products/Debug-iphonesimulator/Oxford Bus.app'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

