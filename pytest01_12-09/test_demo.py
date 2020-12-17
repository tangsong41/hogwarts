# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:42
# @Author  : tangsong
# @File    : test_demo.py

import pytest


def add_function(a, b):
    return a + b


# @pytest.mark.parametrize(
#     "a,b,expected",
#     [
#         (3, 5, 8),
#         (-1, -2, -3),
#         (1000, 1000, 2000)
#     ],
#     ids=["int", "minus", "bigint"]
# )
# def test_add(a, b, expected):
#     assert add_function(a, b) == expected
#

@pytest.mark.parametrize("a", (1, 2))
@pytest.mark.parametrize("b", (3, 4))
def test_add_1(a, b):
    print("测试用例组合 a->%s,b->%s" % (a, b))









