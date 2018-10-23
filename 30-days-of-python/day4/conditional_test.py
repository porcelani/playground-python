# coding: utf-8


def test_if_conditional():
    is_day = True
    is_night = False

    output = ""
    if is_day:
        output = "Is day"
    elif is_night:
        output = "Is Night"

    assert output is "Is day"


def test_isinstance():
    list = [True, False, "Text 1", 1, 2, "Other Text"]
    list_b = []
    list_n = []

    for item in list:
        if isinstance(item, bool):
            list_b.append(item)
        if isinstance(item, int):
            list_n.append(item)

    assert len(list_b) is 2
    assert len(list_n) is 4
