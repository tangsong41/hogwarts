# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: contact_page.py
@time: 2021/01/06
"""
from selenium.webdriver.common.by import By

from test_web01.po.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member= (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    def goto_add_member(self):
        # 解决循环导入的问题
        from test_web01.po.add_member_page import AddMember
        """
        添加成员操作
        :return:
        """

        # 添加显示等待，保证按扭可以点击
        # WebDriverWait(self.driver, 9).until(
        #     expected_conditions.element_to_be_clickable(self._location_goto_add_member))
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return:
        """
        member_list = self.finds(*self._location_member_list)
        # 列表推导式
        member_list_res = [i.text for i in member_list]
        return member_list_res










