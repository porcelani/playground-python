# coding: utf-8
from day7.Dog import Dog


def test_class():
    obj = Dog()
    assert obj.name == "Rex"
    assert obj.noise == "Grunt"
    assert obj.make_noise() == "Grunt"
