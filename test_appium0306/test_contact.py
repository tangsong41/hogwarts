# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_contact.py
@time: 2021/01/03
"""
from appium import webdriver
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        # #启动app时不要清除app里的原有的数据
        desired_caps['noReset'] = "True"
        # 设置页面等待空闲状态的时间
        desired_caps['settings[waitForIdleTimeout]'] = 0
        # desired_caps['fullReset'] = False   #.launch.WwMainActivity
        #desired_caps['appActivity'] = '.enterprise.attendance.controller.AttendanceActivity2'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待 ，
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_contact(self):
        # xpath
        contact_ele = self.driver.find_element(MobileBy.XPATH,
                                               "//*[@text='通讯录' and @resource-id ='com.tencent.wework:id/elq']")
        contact_ele.click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        add_new_ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']")
        add_new_ele.click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/..//*[@text='必填']").send_keys("tangsong")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '性别')]/..//*[@text='男']").click()

        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys("13347700000")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
















