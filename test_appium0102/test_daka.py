# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_daka.py
@time: 2021/01/01
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time

from selenium.webdriver.support.wait import WebDriverWait


class TestDaka:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['noReset'] = "True"
        # 设置页面等待空闲状态的时间
        desired_caps['settings[waitForIdleTimeout]'] = 0
        # desired_caps['fullReset'] = False   #.launch.WwMainActivity
        #desired_caps['appActivity'] = '.enterprise.attendance.controller.AttendanceActivity2'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    # def test_daka01(self):
    #     TouchAction(self.driver).tap(x=453, y=1244).perform()
    #     TouchAction(self.driver).tap(x=221, y=950).perform()
    #     TouchAction(self.driver).tap(x=134, y=941).perform()
    #     TouchAction(self.driver).tap(x=592, y=706).perform()

    # def test_daka02(self):
        # el4 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.TextView")
        # el4.click()
        # time.sleep(5)
        # el5 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[10]")
        # el5.click()
        # time.sleep(10)

    #def test_daka03(self):
        # el3 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.TextView")
        # el3.click()
        # time.sleep(3)
        # el6 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[10]/android.widget.TextView")
        # el6.click()
        # time.sleep(3)
        # el7 = self.driver.find_element_by_id("com.tencent.wework:id/eeh")
        # el7.click()
        # time.sleep(3)
        # el8 = self.driver.find_element_by_id("com.tencent.wework:id/alq")
        # el8.click()

    def test_daka_commit(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        #滚动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # time.sleep(2)
        print(self.driver.page_source)
        WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功" in x.page_source)

        assert "外出打卡成功" in self.driver.page_source






