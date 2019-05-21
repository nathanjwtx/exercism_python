import random as r
import math


class Character:
    traits = {
        "strength": 0,
        "dexterity": 0,
        "constitution": 0,
        "intelligence": 0,
        "wisdom": 0,
        "charisma": 0
    }

    def __init__(self):
        for x in self.traits:
            self.traits[x] = r.randint(3, 18)
        self.hitpoints = 0

    @property
    def hitpoints(self):
        return self.__hitpoints

    @hitpoints.setter
    def hitpoints(self, hitpoints):
        self.__hitpoints = 10 + math.floor((self.constitution - 10) / 2)

    @property
    def strength(self):
        return self.traits["strength"]

    @property
    def dexterity(self):
        return self.traits["dexterity"]

    @property
    def constitution(self):
        return self.traits["constitution"]

    @property
    def intelligence(self):
        return self.traits["intelligence"]

    @property
    def wisdom(self):
        return self.traits["wisdom"]

    @property
    def charisma(self):
        return self.traits["charisma"]

    def ability(self):
        return self.traits[list(self.traits.keys())[r.randint(0, 6)]]


def modifier(constitution):
    return math.floor((constitution - 10) / 2)
