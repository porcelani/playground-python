# coding: utf-8
import csv


def get_leanth(file_path):
    # with open(file_path, "r") as csvfile:
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)


def find_data(id=None, name=None, email=None):
    file_path = "data.csv"
    fieldNames = ["id", "name", "email"]
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print row
            if id is not None:
                if int(id) == int(row["id"]):
                    return row
            if name is not None:
                if name == row["name"]:
                    return row
            if email is not None:
                if email == row["email"]:
                    return row


def test_find_danilo():
    entity = find_data(1)

    assert entity["name"] == "Danilo"
    assert entity["email"] == "porcelani@gmail.com"


def test_find_miguel():
    entity = find_data(9)

    assert entity["name"] == "Miguel"
    assert entity["email"] == "miguel@gmail.com"
