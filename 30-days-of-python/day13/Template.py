# coding: utf-8
import os


class Template:

    def __init__(self):
        pass

    def get_format(self, context):
        return self.get_template().format(**context)

    def get_format_text(self, name, age):
        return self.get_template().format(name=name, age=age)

    def get_template(self):
        file_path = self._get_template_path()
        return open(file_path).read()

    def _get_template_path(self):
        file_ = "template/message.txt"
        file_path = os.path.join(os.getcwd(), file_)
        return file_path
