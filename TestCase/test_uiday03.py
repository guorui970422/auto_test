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
        # 点击订单 (//span[contains(text(),'商品')])[1]
        base.click("点击订单","(//span[contains(text(),'订单')])[1]")
        # 点击订单列表 //span[contains(text(),'添加商品')]
        base.click("点击订单列表", "(//span[contains(text(),'订单列表')])[1]")
        assert "收货人" in driver.page_source
        time.sleep(2)
        # 订单状态选择代发货 (//input[@class='el-input__inner'])[4]
        base.click("订单状态选择代发货","(//input[@class='el-input__inner'])[4]")
        base.click("状态选择代发货","//span[contains(text(),'待发货')]")
        # 点击查询搜索 //button[@class='el-button el-button--primary el-button--small']
        base.click("点击查询搜索","//button[@class='el-button el-button--primary el-button--small']")
        # 选择第一条订单，点击订单发货(//button[@class='el-button el-button--default el-button--mini'])[3]
        base.click("选择第一条订单，点击订单发货","(//button[@class='el-button el-button--default el-button--mini'])[3]")
        # 选择配送方式 (//input[@class='el-input__inner'])[2]
        base.click("选择配送方式","//input[@placeholder='请选择物流公司']")
        base.click("选择快递公司","//span[contains(text(),'顺丰')]")
        # 输入物流单号
        base.send_keys("输入物流单号","(//input[@class='el-input__inner'])[2]","1234567887654321")
        # 点击确定 //button[@class='el-button el-button--primary']
        base.click("点击确定","(//span[contains(text(),'确定')])[1]")
        # 点击确定提示 //button[@class='el-button el-button--default el-button--small el-button--primary ']
        base.click("点击确定提示","(//span[contains(text(),'确定')])[2]")
        # 获取提示文本并断言
        print(driver.page_source)
        assert  "发货成功" in driver.page_source
        time.sleep(2)


