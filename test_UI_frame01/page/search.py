# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: search.py
@time: 2021/01/10
"""
from selenium.webdriver.common.by import By

from test_UI_frame01.util.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("腾讯")
        return True












