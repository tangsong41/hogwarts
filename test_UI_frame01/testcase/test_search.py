# -*- coding: utf-8 -*-
"""
@author:tangsong
@file: test_search.py
@time: 2021/01/10
"""
from test_UI_frame01.util.app import App


class TestSearch:
    def setup(self):
        self.app = App()

    def test_search(self):
        self.app.start().goto_main().goto_market().goto_search().search()











