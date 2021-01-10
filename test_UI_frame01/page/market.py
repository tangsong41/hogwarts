# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: market.py
@time: 2021/01/10
"""
from selenium.webdriver.common.by import By

from test_UI_frame01.page.search import Search
from test_UI_frame01.util.base_page import BasePage




class Market(BasePage):
    def goto_search(self):
        self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        return Search(self.driver)










