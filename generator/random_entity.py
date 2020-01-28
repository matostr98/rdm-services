from typing import List

from generator.probability_entity import ProbabilityEntity


class RandomEntity:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + " " + str(self.value)
