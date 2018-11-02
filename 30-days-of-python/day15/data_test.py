# coding: utf-8
import csv


def get_leanth(file_path):
    # with open(file_path, "r") as csvfile:
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)


def append_data(file_path, name, email):
    fieldNames = ["id", "name", "email"]
    next_id = get_leanth(file_path)
    with open('data.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

        if next_id == 0:
            next_id = 1
            writer.writeheader()

        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email
        })


def test_append_with_dictionary():
    append_data("data.csv", "Danilo", "porcelani@gmail.com")
