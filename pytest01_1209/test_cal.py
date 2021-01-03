# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:39
# @Author  : tangsong
# @File    : test_cal.py

import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print('开始计算')

    def teardown_calss(self):
        print('结束计算')

    @pytest.mark.parametrize(
        "a,b,expect",
        [(1, 2, 3), (-1, -2, -3), (1000, 1000, 2000)],
        ids=["int", "minus", "big"]
    )
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize(
        "a,b,expect",
        [(3, 2, 1), (-3, -2, -1), (2000, 1000, 1000)],
        ids=["int", "minus", "big"]
    )
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize(
        "a,b,expect",
        [(3, 2, 6), (-3, -2, 6), (100, 100, 10000)],
        ids=["int", "minus", "big"]
    )
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize(
        "a,b,expect",
        [(6, 2, 3), (-6, -2, 3), (10000, 100, 100)],
        ids=["int", "minus", "big"]
    )
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)









