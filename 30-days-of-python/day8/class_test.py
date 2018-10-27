# coding: utf-8
import pytest

from day8.Dog import Dog


def test_class():
    obj = Dog()

    assert obj.name is None

    obj.change_name(animal_name="Rex")

    assert obj.name == "Rex"
    assert obj.noise == "Grunt"

    assert obj.make_noise == "Grunt"
    with pytest.raises(TypeError):
        obj.make_noise()
