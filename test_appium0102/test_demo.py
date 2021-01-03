# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_demo.py
@time: 2020/12/31
"""
from appium import webdriver

class testDemo:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = 'com.android.settings.Settings'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub/sessions', desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        el7 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
        el7.click()
        el8 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout")
        el8.click()
        el9 = self.driver.find_element_by_id("android:id/button1")
        el9.click()
        el10 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.TextView")
        el10.click()
        el11 = self.driver.find_element_by_accessibility_id("向上导航")
        el11.click()














