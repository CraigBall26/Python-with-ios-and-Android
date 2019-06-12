#from bus_app_flow_locators.android_flow_locators import *
from appium import webdriver
from bus_app_android_main.practice_main import *
from math import log
import logging
import threading
import time
import logging

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['avd'] = 'Nexus_6'
desired_caps['avdLaunchTimeout'] = 150000
desired_caps['app'] = '/Users/craigball/eclipse-workspace/bus_app_automation/bus_app_android_apks/app-oxfordbuses-staging.apk'
desired_caps['appPackage']="com.oxford.bus"
desired_caps['appActivity' ]=".activities.splash.SplashActivity"

print(desired_caps)
logging.error('raised an error')

#pytest -o log_cli=true prints logs out in tests
#set up config file
#put first test into test file
#put logger info in test
#show we can fail if elemets arent there
#add 2nd test
#

def test_1():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def test_eggs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True
    
    open_app_splash.deny_gps_button().click()
home_page.deny_gps_button().click()
try:
    signup_process_password_page.continue_button()
except ElementNotVisibleException:
    raise TypeError
