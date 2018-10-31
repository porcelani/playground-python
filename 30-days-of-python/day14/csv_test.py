# coding: utf-8
import csv


def test_open():
    with open('eggs.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def test_append():
    with open('append.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Spam'] * 5 + ['Baked Beans'])
        writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def test_append_with_dictionary():
    with open('append_with_dictionary.csv', 'a') as csvfile:
        fieldNames = ["id", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerow({"id": 123, "title": "New Title"})
