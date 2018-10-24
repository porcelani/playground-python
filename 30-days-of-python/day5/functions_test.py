# coding: utf-8

def test_functions_sort_in_number_list():
    number_list = [10, 1000, 100, 1]

    number_list.sort()

    assert number_list == [1, 10, 100, 1000]

    number_list.sort(reverse=True)

    assert number_list == [1000, 100, 10, 1]


def test_functions_sorted_in_number_list():
    number_list = [10, 1000, 100, 1]

    number_list = sorted(number_list)

    assert number_list == [1, 10, 100, 1000]

    number_list = sorted(number_list, reverse=True)

    assert number_list == [1000, 100, 10, 1]


def test_functions_sort_in_string_list():
    string_list = ["BB", "ba", "ad", "aA"]

    string_list.sort()

    assert string_list == ['BB', 'aA', 'ad', 'ba']

    string_list.sort(key=str.lower)

    assert string_list == ['aA', 'ad', 'ba', 'BB']

    string_list.sort(key=str.lower, reverse=True)

    assert string_list == ['BB', 'ba', 'ad', 'aA']


def test_functions_sorted_in_string_list():
    string_list = ["BB", "ba", "ad", "aA"]

    string_list = sorted(string_list)

    assert string_list == ['BB', 'aA', 'ad', 'ba']

    string_list = sorted(string_list, key=str.lower)

    assert string_list == ['aA', 'ad', 'ba', 'BB']

    string_list = sorted(string_list, key=str.lower, reverse=True)

    assert string_list == ['BB', 'ba', 'ad', 'aA']

