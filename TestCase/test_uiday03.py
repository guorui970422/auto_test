#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import pytest


from selenium import webdriver
from Common import Assert

assertions = Assert.Assertions
from Common.baseui import baseUI
from Common.read_excel import *





class Test_ui_aout:
    # def test_newbee(self,driver):
    #     base = baseUI(driver)
    #     # 打开网址
    #     driver.get("http://192.168.1.128/#/login")
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












    def test_UI6(self,driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.1.128:8090/#/login")
        # 点击输入账户
        base.send_keys("点击输入账户","//input[@name='username']","")
        # 点击输入密码
        base.send_keys("点击输入密码", "//input[@name='password']", "")
        # 点击登录
        base.click("点击登录","//span[contains(text(),'登录')]")
        # assertions.assert_code()
        assert "首页" in driver.page_source
        time.sleep(2)
        # 点击商品列表 (//span[contains(text(),'商品')])[1]
        base.click("点击商品列表","(//span[contains(text(),'商品')])[1]")
        # 点击添加商品 //span[contains(text(),'添加商品')]
        base.click("点击添加商品", "//span[contains(text(),'添加商品')]")
        assert "商品分类" in driver.page_source
        time.sleep(2)
        # 点击商品分类下拉框//span[@class='el-cascader__label']
        base.click("点击商品分类下拉框","//span[@class='el-cascader__label']")
        # 点击商品分类(//li[@class='el-cascader-menu__item el-cascader-menu__item--extensible'])[1]
        base.click("点击商品分类","(//li[@class='el-cascader-menu__item el-cascader-menu__item--extensible'])[1]")
        # 点击男鞋 //li[contains(text(),'男鞋')]
        base.click("点击男鞋","//li[contains(text(),'男鞋')]")
        # 点击商品名称
        base.send_keys("点击商品名称","(//input[@class='el-input__inner'])[2]","我想面试")
        time.sleep(2)


