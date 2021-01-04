# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_contact_commit.py
@time: 2021/01/03
"""
import random

from test_appium0306.page.app import App


class Test_ContactCommit:
    def setup(self):
        self.app = App()
        self.app.start()
        self.main = self.app.goto_main()

    def test_contact_addmember(self):
        ran = random.randint(100, 999)
        name = "tangsong" + str(ran)
        sex = "女"
        phone_number = "13347700"+ str(ran)
        result = self.main.goto_address().click_addmember().add_member_manual().add_contact_commit(name, sex, phone_number)










