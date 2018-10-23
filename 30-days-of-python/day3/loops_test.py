# coding: utf-8


def test_for_loop():
    item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    output1 = 0
    for item in item_list:
        output1 += item
    assert output1 is 45
