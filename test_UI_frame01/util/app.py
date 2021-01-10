# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: app.py
@time: 2021/01/10
"""
from appium import webdriver

from test_UI_frame01.page.main import Main
from test_UI_frame01.util.base_page import BasePage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动app
            # 定义了一个字典
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            # noReset 保留缓存， 比如登录状态 .view.WelcomeActivityAlias
            caps["noReset"] = "True"
            # 关键  localhost:4723  本机ip:server端口
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
            # self.driver.start_activity(package,activity)

        return self

    def restart(self):
        # 重启 app
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        # 停止 app
        self.driver.quit()

    def goto_main(self):
        # 进入到首页
        return Main(self.driver)













