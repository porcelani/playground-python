# coding: utf-8
import pytest


def test_create():
    city_dictionary = {
        "Maringá": "Cidade Canção ",
        "Rio de Janeiro": "Cidade Maravilhosa"
    }
    assert len(city_dictionary) is 2

    city_dictionary["São Paulo"] = "Cidade da Garoa"

    assert len(city_dictionary) is 3

    with pytest.raises(KeyError):
        city_dictionary["Different Key"]
