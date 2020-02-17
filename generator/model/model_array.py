import random

from generator.model.model_entity import ModelEntity


class ModelArray(ModelEntity):
    def __init__(self, model_description):
        super().__init__(model_description)
        self.weights = None
        self.array = model_description['array']

        if 'weights' in model_description:
            self.weights = model_description['weights']
        if 'count' in model_description:
            self.count = model_description['count']

    def generate_values(self):
        value = random.choices(self.array, weights=self.weights, k=self.count)

        if len(value) == 1:
            value = value[0]

        return self.key, value
