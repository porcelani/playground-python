# coding: utf-8


def filter_number(list):
    string_list = []
    number_list = []

    method_name(list, number_list, string_list)

    return number_list


def filter_string(list):
    string_list = []
    number_list = []

    method_name(list, number_list, string_list)

    return string_list


def method_name(list, number_list, string_list):
    for item in list:
        if isinstance(item, int) or isinstance(item, float):
            number_list.append(item)
        elif isinstance(item, str):
            string_list.append(item)


def test_filter():
    list = ["BB", "ba", 1000, 100, 1, "ad", "aA", 10, 1.2]

    assert filter_string(list) == ['BB', 'ba', 'ad', 'aA']
    assert filter_number(list) == [1000, 100, 1, 10, 1.2]
