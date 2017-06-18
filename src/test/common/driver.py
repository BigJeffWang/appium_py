# coding:utf-8
from appium import webdriver


def remote():
    url = '127.0.0.1:4444'
    desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'appPackage': 'com.android.contacts',
            'appActivity': '.activities.PeopleActivity',
            'deviceName': 'YVF4C15811000302',
        }
    driver = webdriver.Remote(url, desired_caps)
    return driver
