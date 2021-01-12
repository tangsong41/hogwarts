# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: main.py
@time: 2021/01/10
"""
from selenium.webdriver.common.by import By

from test_UI_frame01.page.market import Market
from test_UI_frame01.util.base_page import BasePage


class Main(BasePage):
    def goto_market(self):
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        print("post_status")
        self.find_and_click(By.XPATH, "//*[@text='行情']")  #//*[@resource-id='com.xueqiu.android:id/tab']
        print("行情")
        return Market(self.driver)







