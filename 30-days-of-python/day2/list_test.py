# coding: utf-8


def test_append():
    city_list = ["Maringá", "Rio de Janeiro"]
    assert len(city_list) is 2
    city_list.append("São Paulo")
    assert len(city_list) is 3
    assert city_list[0] is "Maringá"
    assert city_list[1] is "Rio de Janeiro"
    assert city_list[2] is "São Paulo"


def test_pop():
    city_list = ["Maringá", "Rio de Janeiro"]
    city_list.pop()
    assert len(city_list) is 1
    assert city_list[0] is "Maringá"


def test_pop_base_position():
    city_list = ["Maringá", "Rio de Janeiro"]
    city_list.pop(0)
    assert len(city_list) is 1
    assert city_list[0] is "Rio de Janeiro"
