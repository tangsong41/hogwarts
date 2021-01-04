# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: main_page.py
@time: 2021/01/03
"""
from appium.webdriver.common.mobileby import MobileBy


from test_appium0306.page.addresss_list_page import AddressListPage
from test_appium0306.page.base_page import BasePage


class MainPage(BasePage):
    """
        首页 PO
        """

    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        # todo 点击通讯录按钮
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id ='com.tencent.wework:id/elq']")
        print("main-commit"+"AddressListPage-begin")
        return AddressListPage(self.driver)


















