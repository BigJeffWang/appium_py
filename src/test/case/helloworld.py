# coding:utf-8
import sys
import os
import unittest
from time import sleep
from appium import webdriver


class HelloWorld(unittest.TestCase):
    def test_addContact(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'appPackage': 'com.android.contacts',
            'appActivity': '.activities.PeopleActivity',
            'deviceName': 'YVF4C15811000302',
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        workPath = os.getcwd() + "\\report\\img\\"
        print workPath
        # 查找创建新联系人按钮
        createContactButton = None
        try:
            # 如果手机没有联系人,则通过create_contact_button来创建.此处通过id查找
            createContactButton = driver.find_element_by_id("com.android.contacts:id/btn_create_new_contact")
        except:
            # 否则通过底部的添加联系人菜单添加
            createContactButton = driver.find_element_by_id("com.android.contacts:id/btn_left")
        # 单击创建
        createContactButton.click()

        # 查看Dialog是否显示
        try:
            dialog = driver.find_element_by_id("android:id/content")
            # 找到本地按钮并保存
            saveLocal = driver.find_element_by_id(
                "com.android.contacts:id/left_button"
            )
            saveLocal.click()
            sleep(2)
        except Exception as e:
            print "no dialog found"
            # print e
            name = driver.find_element_by_name(u"姓名")
            name.click()
            name.send_keys("appiumtest")
            # 输入电话号码
            teleNumber = driver.find_element_by_name(u"电话号码")
            teleNumber.click()
            teleNumber.send_keys("13812345678")
            # 保存截屏
            driver.save_screenshot(workPath+"afterinput.png")
            # 完成单击
            completeButton = driver.find_element_by_id("android:id/icon2")
            completeButton.click()

        barTitle = driver.find_element_by_id("com.android.contacts:id/name")
        self.assertEqual(barTitle.text, u"appiumtest")
        numTitle = driver.find_element_by_id("com.android.contacts:id/data")
        self.assertEqual(numTitle.text, u"138 1234 5678")
        driver.save_screenshot(workPath+"newContact.png")

        sleep(3)
        driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
