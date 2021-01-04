# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: member_invite_menu_page.py
@time: 2021/01/03
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium0306.page.base_page import BasePage
from test_appium0306.page.contact_add import ContactAdd


class MemberInviteMenuPage(BasePage):
    """
    添加成员 PO
    """
    def add_member_manual(self):
        """
        手动添加成员信息
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        print("MemberInviteMenuPage-commit" + "ContactAdd-begin")
        return ContactAdd(self.driver)











