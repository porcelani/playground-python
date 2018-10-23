# coding: utf-8
import pytest


def test_create():
    city_tuples = (
        ("Maringá", "Cidade Canção"),
        ("Rio de Janeiro", "Cidade Maravilhosa")
    )
    assert len(city_tuples) is 2
    assert city_tuples[0] == ("Maringá", "Cidade Canção")
    assert city_tuples[0][0] == "Maringá"

    with pytest.raises(IndexError):
        city_tuples[3][3]