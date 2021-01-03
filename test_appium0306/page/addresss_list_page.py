# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: addresss_list_page.py
@time: 2021/01/03
"""
from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage

from test_appium0306.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录 PO
    """
    def click_addmember(self):
        """
        添加成员
        :return:
        """
        # self.scroll_find_click("添加成员")
        self.swip_find_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return MemberInviteMenuPage(self.driver)











