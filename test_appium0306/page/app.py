# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: app.py
@time: 2021/01/03
"""
from appium import webdriver

from test_appium0306.page.base_page import BasePage
from test_appium0306.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps["ensureWebviewsHavePages"] = True
            # #启动app时不要清除app里的原有的数据
            desired_caps['noReset'] = "True"
            # 设置页面等待空闲状态的时间
            desired_caps['settings[waitForIdleTimeout]'] = 0
            # desired_caps['fullReset'] = False   #.launch.WwMainActivity
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else :
            # 启动 但是不是重复执行上面内容
            self.driver.launch_app()
        # 操作，在 10 内，每 0.5 s 查找一次元素
        self.driver.implicitly_wait(10)
        print("app-commit")
    def goto_main(self):
        print("main-begin")
        return MainPage(self.driver)








