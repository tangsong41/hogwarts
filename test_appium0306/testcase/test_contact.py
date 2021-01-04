# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_contact.py
@time: 2021/01/03
"""
from test_appium0306.page.app import App


def test_contact_addmember():
    app = App()
    app.start()
    result =  app.goto_main().goto_address().click_addmember().add_member_manual().add_contact()





















