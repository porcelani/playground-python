# coding: utf-8
import os


def test_print_hello_world():
    path_cwd = os.path.join(os.getcwd(), "file_name.csv")

    assert path_cwd == "/home/porcelani/workspace/git/playground-python/30-days-of-python/day18/file_name.csv"

    path_dirname = os.path.join(os.path.dirname(__file__), "file_name.csv")

    assert path_dirname == "/home/porcelani/workspace/git/playground-python/30-days-of-python/day18/file_name.csv"
