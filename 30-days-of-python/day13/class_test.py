# coding: utf-8
from day13.Template import Template


def test_class():
    obj = Template()

    assert obj.get_format_text("Danilo", "31") == "Hi my name is Danilo and I'm 31 year old.\n"
