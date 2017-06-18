# coding:utf-8

from selenium import webdriver
from time import sleep
from base_util import get_real_path


# 截图函数
def insert_img(driver_param, file_name):
    filePath = get_real_path('/report/img/' + file_name)
    driver_param.get_screenshot_as_file(filePath)


if __name__ == "__main__":
    driver = webdriver.Ie()
    driver.get("https://www.baidu.com")
    sleep(3)
    insert_img(driver, 'test2.png')
    driver.quit()
