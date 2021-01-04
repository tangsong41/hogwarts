# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: contact_add.py
@time: 2021/01/03
"""
import random

from appium.webdriver.common.mobileby import MobileBy

from test_appium0306.page.base_page import BasePage


class ContactAdd(BasePage):
    """
    成员信息编辑
    """

    def add_contact(self):
        """
        添加信息
        :return:
        """
        print("attr-Add-begin")
        ran = random.randint(100, 999)
        name = "tangsong" + str(ran)
        photo = "13347700"+ str(ran)
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text, '姓名')]/..//*[@text='必填']", name)
        self.find_and_click(MobileBy.XPATH,
                            "//*[contains(@text, '性别')]/..//*[@text='男']")
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text, '手机')]/..//*[@text='手机号']",
                           photo)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        print("完成")
        return True

    def add_contact_commit(self,name,sex,phone):
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text, '姓名')]/..//*[@text='必填']", name)
        self.find_and_click(MobileBy.XPATH,
                            "//*[contains(@text, '性别')]/..//*[@text='男']")
        if sex == "男":
            #WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            #self.find(MobileBy.XPATH, "//*[@text='男']").click()
            self.wait_for(MobileBy.XPATH, "//*[@text='女']")
            self.find_and_click(MobileBy.XPATH, "//*[@text='男']")
        else:
            self.wait_for(MobileBy.XPATH, "//*[@text='女']")
            self.find_and_click(MobileBy.XPATH, "//*[@text='女']")

        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text, '手机')]/..//*[@text='手机号']",
                           phone)

        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        print("完成")
        return True









