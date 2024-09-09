from datetime import date
import random


class Dice:
    def roll(self):
        return random.randint(1, 6)


class Person:
    def __init__(self, date_of_birth):
        self._dob = date_of_birth

    def age(self):
        td = date.today() - self._dob
        return td.days // 365
