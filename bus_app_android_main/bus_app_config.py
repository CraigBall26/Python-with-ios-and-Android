from appium import webdriver
import datetime
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
import re
from _ast import Try
from selenium.common.exceptions import ElementNotVisibleException
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
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)

def get_signup_code(created_email):
    client = MailosaurClient("HTHVZPgrEGS4NSN")
    criteria = SearchCriteria()
    criteria.sent_to = created_email
    results = client.messages.wait_for("3chdjbxe", criteria)
    signupRegex = re.search(r"\b[012345679bcdfghjkmnpqrstvwxyzCDFGHJKLMNPQRSTVWXYZ]{4}\b", results.subject)
    return signupRegex.group()

def get_random_email():
    datenow = datetime.datetime.now()
    return "{}.3chdjbxe@mailosaur.io".format(datenow.strftime("%m%d%H%M%S"))

def get_method_added_email(created_email):
    client = MailosaurClient("HTHVZPgrEGS4NSN")
    criteria = SearchCriteria()
    criteria.sent_to = created_email
    results = client.messages.wait_for("3chdjbxe", criteria)
    signupRegex = re.search(r"payment method", results.subject)
    return signupRegex.group()
    



#***********************Customer Details *************************
firstname = "Automation"
surname = "Test"
password = "autotestcb123"
