# coding: utf-8
import datetime


def test_string():
    text = "My name is {name}".format(name="Porcelani")

    assert text == "My name is Porcelani"

    text = "My name is {0}".format("Porcelani")

    assert text == "My name is Porcelani"


def test_string_triple_quoted():
    text = '''
My name is {name}
My name is {name}
'''.format(name="Porcelani")

    assert text == "\nMy name is Porcelani\nMy name is Porcelani\n"


def test_date():
    date = datetime.date.today()
    today = "{dd}/{mm}/{yyyy}".format(dd=date.day, mm=date.month, yyyy=date.year)
    assert isinstance(today, str)
