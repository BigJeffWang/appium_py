# coding:utf-8
from appium import webdriver
from time import sleep
from ...utils.base_util import get_ymd_microsecond_time, get_real_path, get_ymd_list_path
from enum import Enum


class ConnectionType(Enum):
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6


class Page(object):
    """
    页面基础类，用于所有页面的继承
    """

    def __init__(self, driver):
        driver = webdriver.Remote()  # TODO
        self._driver = driver
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'appPackage': 'com.android.contacts',
            'appActivity': '.activities.PeopleActivity',
            'deviceName': 'YVF4C15811000302',
        }

    def find_element(self, control_info):
        """
        整合给定控件的xpatch, id 或者name来查找控件
        :param control_info: 页面元素
        :return: 返回一个字符串
        """
        if control_info.startswith('//'):
            element = self._driver.find_element_by_xpath(control_info)
        elif ':id/' in control_info or ':string/' in control_info:
            element = self._driver.find_element_by_id(control_info)
        else:
            try:
                element = self._driver.find_element_by_name(control_info)
            except:
                element = self._driver.find_element_by_class_name(control_info)
            else:
                print "The element was not found on the page"

        return element

    def find_elemens(self, control_info):
        """
        整合给定控件的xpatch, id 或者name来查找控件
        :param control_info: 页面元素
        :return: 返回一个列表
        """
        if control_info.startswith('//'):
            element = self._driver.find_elements_by_xpath(control_info)
        elif ':id/' in control_info or ':string/' in control_info:
            element = self._driver.find_elements_by_id(control_info)
        else:
            try:
                element = self._driver.find_elements_by_name(control_info)
                if not len(element):
                    raise BaseException("not find element by name")
            except:
                element = self._driver.find_elements_by_class_name(control_info)
            else:
                print "The element was not found on the page"
        return element

    def find_element_in_parent_element(self, parent_element, child_element_info):
        """
        在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件
        :param parent_element:
        :param child_element_info:
        :return: 如果找到控件，返回第一个
        """
        if child_element_info.startwith('//'):
            element = parent_element.find_element_by_xpath(child_element_info)
        elif ':id' in child_element_info:
            element = parent_element.find_element_by_id(child_element_info)
        else:
            try:
                element = parent_element.find_element_by_name(child_element_info)
            except:
                element = parent_element.find_element_by_class_name(child_element_info)
            else:
                print "The element was not found on the page"
        return element

    def find_elements_in_parent_element(self, parent_element, child_element_info):
        """
        在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件
        :param parent_element:
        :param child_element_info:
        :return: 如果找到控件，返回是所有符合
        """
        if child_element_info.startwith('//'):
            element = parent_element.find_elements_by_xpath(child_element_info)
        elif ':id' in child_element_info:
            element = parent_element.find_elements_by_id(child_element_info)
        else:
            try:
                element = parent_element.find_elements_by_name(child_element_info)
                if not len(element):
                    raise BaseException("not find element by name")
            except:
                element = parent_element.find_elements_by_class_name(child_element_info)
            else:
                print "The element was not found on the page"
        return element

    def find_element_by_uiautomator(self, uia_string):
        """
        通过UIAutomator的uia_string来查找控件
        参考http://developer.android.com/
        tools/help/uiautomator/UiSelector.html#fromParent%28com.android.uiautomator.core.UiSelector%29
        :param uia_string:
        :return: 找到的控件
        """
        return self._driver.find_element_by_android_uiautomator(uia_string)

    def find_elements_by_uiautomator(self, uia_string):
        """
        通过UIAutomator的uia_string来查找控件
        参考http://developer.android.com/
        tools/help/uiautomator/UiSelector.html#fromParent%28com.android.uiautomator.core.UiSelector%29
        :param uia_string:
        :return: 找到的控件
        """
        return self._driver.find_elements_by_android_uiautomator(uia_string)

    def flick(self, x1, y1, x2, y2):
        """
        滑动操作 self.flick(50, 50, 400, 400)
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        """
        self._driver.flick(x1, y1, x2, y2)

    def swip(self, x1, y1, x2, y2, peroid):
        """
        滑动操作的起点和终点的坐标
         - peroid: 多长时间内完成该操作,单位是毫秒
        self.swipe(50, 50, 400, 400, 500)
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param peroid:
        :return:
        """
        self._driver.swipe(x1, y1, x2, y2, peroid)

    def tap(self, x, y, duration=None):
        """
        点击操作 self.tap(100, 20, 500)
         - druation 长按多少秒
        :param duration:
        :param x:
        :param y:
        :return:
        """
        self._driver.tap([(x, y)], duration)

    def click_element(self, element_info):
        """
        点击某一个控件，如果改控件不存在则会抛出异常
        :param element_info:
        :return:
        """
        element = self.find_element(element_info)
        element.click()

    def get_text_element(self, element_info):
        """
        获取某个控件显示的文本，如果该控件不能找到则会抛出异常
        :param element_info:
        :return:
        """
        element = self.find_element(element_info)
        return element.text

    def clear_text_element(self, element_info):
        """
        清除文本框里面的文本
        :param element_info:
        :return:
        """
        element = self.find_element(element_info)
        element.clear()

    def press_backkey(self):
        """
        code码参考Android的官网的keycode
        :return:
        """
        self._driver.press_keycode(4)

    def wait_for_element(self, element_info, period):
        """
        等待某个控件显示
        :param element_info:
        :param period:
        :return:
        """
        for i in range(0, period):
            sleep(1)
            try:
                self.find_element(element_info)
                return
            except:
                continue
        raise Exception("Cannot find %s in %d seconds" % (element_info, period))

    def wait_for_element_notpresent(self, element_info, period):
        """
        等待某个控件不显示
        :param element_info:
        :param period:
        :return:
        """
        for i in range(0, period):
            sleep(1)
            if not self.find_element(element_info):
                return
        raise Exception("Cannot find %s in %d seconds" % (element_info, period))
    
    def check_element_is_shown(self, element_info):
        """
        判断某个控件是否显示
        :param element_info: 
        :return: 
        """
        try:
            self.find_element(element_info)
            return True
        except:
            return False
    
    def check_element_shown_in_Parent_element(self, parent_element, child_element_info):
        """
        判断某个控件是否显示在另外一个控件中
        :param parent_element: 
        :param child_element_info: 
        :return: 
        """
        try:
            self.find_elements_in_parent_element(parent_element, child_element_info)
            return True
        except:
            return False
        
    def check_element_is_select(self, element_info):
        """
        判断某个控件是否被选中
        :param element_info: 
        :return: 
        """
        element = self.find_element(element_info)
        return element.is_selected()

    def check_element_is_checked(self, element_info):
        """
        判断某个开关控件是否被选中
        :param element_info:
        :return:
        """
        element = self.find_element(element_info)
        if element.get_attribute("checked") == "false":
            return False
        else:
            return True

    def check_element_is_enabled(self,element_info):
        """
        判断摸个控件是否enabled提供
        :param element_info:
        :return:
        """
        element = self.find_element(element_info)
        return element.get_attribute("enabled")

    def get_current_activity(self):
        """
        获取当前的Activity
        :return:
        """
        return self._driver.current_activity

    def wait_for_activity(self, activity_name, period):
        """
        等待某一个Activity显示
        备注：不确定是否适用于ios
        :param activity_name:
        :param period:
        :return:
        """
        for i in range(0, period):
            sleep(1)
            try:
                if activity_name in self.get_current_activity():
                    return
            except:
                continue
        raise Exception("Cannot find the activity %s in %d seconds" % (activity_name, period))

    def save_screen_shot(self):
        """
        保存当前手机的屏幕截图到电脑上指定位置
        :param save_path:
        :return:
        """
        fileName = get_ymd_microsecond_time() + ".png"  # 20170617150346654000.png
        ymdListPath = get_ymd_list_path()  # 2017/06/17/
        filePath = get_real_path("/report/img/" + ymdListPath + fileName)
        self._driver.save_screenshot(filePath)
        return filePath

    def launch_app(self):
        """
        启动测试程序
        :return:
        """
        self._driver.launch_app()

    def close_app(self):
        """
        关闭测试程序
        :return:
        """
        self._driver.close_app()

    def get_device_os(self):
        """
        获取测试设备的OS
        :return:
        """
        return self.desired_caps['platformName']

    def enable_wifi_only(self):
        """
        只打开wifi连接
        :return:
        """
        if (self._driver.network_connection & 0x2) == 2:
            return
        else:
            self._driver.network_connection(ConnectionType.WIFI_ONLY)

    def enable_data_only(self):
        """
        只打开数据连接
        :return:
        """
        if int(self._driver.network_connection & 4) == 4:
            return
        else:
            self._driver.set_network_connection(ConnectionType.DATA_ONLY)

    def disable_all_connection(self):
        """
        关闭所有网络连接
        :return:
        """
        self._driver.set_network_connection(ConnectionType.NO_CONNECTION)

    def enable_all_connection(self):
        """
        打开所有的网络连接
        :return:
        """
        self._driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

    def get_all_context(self):
        """
        获取当前会话session所有可以用的上下文
        :return:
        """
        return self._driver.contexts()

    def get_current_context(self):
        """
        获取当前会话session正在使用的上下文
        :return:
        """











































