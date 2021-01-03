# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_contact.py
@time: 2021/01/03
"""
from test_appium0306.page.app import App


class TestContact:

    def test_contact(self):
        self.app = App()
        self.main = self.app.start().goto_main()
        result = self.main.goto_address().click_addmember().add_member_menual().add_contact()





















