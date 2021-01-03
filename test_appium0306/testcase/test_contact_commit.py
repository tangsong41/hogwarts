# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_contact_commit.py
@time: 2021/01/03
"""
from test_appium0306.page.app import App


class Test_ContactCommit:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        ran = random.randint(0, 99)
        name = "tangsong" + ran
        sex = "女"
        phone_number = "13347700000"
        result = self.main.goto_address().click_addmember().add_member_menual().add_contact_commit(name, sex, phone_number)










