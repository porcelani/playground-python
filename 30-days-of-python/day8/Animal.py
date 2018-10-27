# coding: utf-8


class Animal:
    noise = "Grunt"
    size = "Large"
    name = None

    def __init__(self):
        pass

    @property
    def make_noise(self):
        return self.noise

    def change_name(self, animal_name):
        self.name = animal_name
