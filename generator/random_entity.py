from typing import List

from generator.probability_entity import ProbabilityEntity


class RandomEntity:
    def __init__(self, key, count: int, values: List[ProbabilityEntity]):
        self.key = key
        self.count = count
        self.values = []
        self.weights = []
        for v in values:
            self.values.append(v)
            self.weights.append(v.weight)

    def __str__(self):
        return str(self.key) + " " + str(self.count) + " " + str(self.values) + " " + str(self.weights)
