import json
from abc import abstractmethod

class ModelEntity:
    def __init__(self, model_description):
        self.key = model_description['key']
        self.count = 1

        if 'count' in model_description:
            self.count = model_description['count']

    @staticmethod
    def parse_model(filepath):
        with open(filepath) as json_file:
            data = json.load(json_file)
            entities = data['model']

            return entities

    @abstractmethod
    def generate_values(self):
        pass
