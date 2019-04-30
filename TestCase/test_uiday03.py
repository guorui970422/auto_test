#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import pytest


from selenium import webdriver

from Common.baseui import baseUI
from Common.read_excel import *





class Test_ui_aout:
    # def test_newbee(self,driver):
    #     base = baseUI(driver)
    #     # 打开网址
    #     driver.get("http://192.168.1.137/#/login")
    #     # 调用baseUI方法
    #     base.click("点击登录按钮", "//span[contains(text(),'登录')]")
    #     base.click("点击残忍拒绝", "//span[contains(text(),'残忍拒绝')]")
    #     base.click("点击登录按钮", "//span[contains(text(),'登录')]")
    #     time.sleep(2)
    #     assert '首页' in driver.page_source
    # def test_aot(self,driver):
    #     print('我曾经跨过山和大海')
    #     driver.quit()
    # l_name = read_excel_list("d:\\fix.xlsx")
    # @pytest.fixture(params=l_name)
    # def name(self, request):
    #     return request.param
    #
    # def test_order_2(self, name):
    #     print(name[0])

        # pass

    l_name = read_excel_list("d:\\fix.xlsx")
    @pytest.fixture(params=l_name)
    def name(self,request):
        return request.param
    def test_fix(self,name):
        print(name[0])
        pass













