# coding:utf-8
import os
import time
import datetime


def get_real_path(add_path=None):
    basePath = os.path.dirname(__file__)
    proIndex = basePath.find("appium_py")
    basePath = basePath[:proIndex] + "appium_py" + add_path
    realPath = os.path.normcase(basePath)
    if not os.path.exists(realPath):
        os.makedirs(realPath, 0755)
    return realPath


def get_relative_path(add_path=None):
    relativePath = os.path.normcase(os.path.join(os.path.dirname(__file__), add_path))
    if not os.path.exists(relativePath):
        os.makedirs(relativePath, 0755)
    return relativePath


def get_ymd_time(form="%Y%m%d%H%I%S"):
    return time.strftime(form, time.localtime())


def get_ymd_microsecond_time():
    return get_ymd_time() + str(datetime.datetime.now().microsecond)


def get_ymd_list_path():
    return get_ymd_time("%Y/%m/%d/")

if __name__ == "__main__":
    # print os.sys.path

    # 测试绝对路径
    # realPath = get_real_path("/log/1/2/logtest.txt")
    # print realPath
    # with open(realPath, "w") as f:
    #     f.write("aaa")

    # 测试相对路径
    # relaPath = get_relative_path("../../log/1/2/logtest2.txt")
    # print relaPath
    # with open(relaPath, "w") as f:
    #     f.write("bbb")

    # 测试 时间 时间+毫秒
    # print get_ymd_microsecond_time()
    # time.sleep(1)
    # print get_ymd_microsecond_time()
    # print get_ymd_list_path()
