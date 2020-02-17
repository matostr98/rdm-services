from attributes.models import MetricsAttributes
from generator.generator import generate_values_dynamically
from generator.model.model_entity import ModelEntity


class AttributesService:
    def __init__(self, sourcefile):
        self.descriptions = ModelEntity.parse_model(sourcefile)

    def generate_attributes(self):
        results = {}

        for desc in self.descriptions:
            key, value = generate_values_dynamically(desc)
            results[key] = value

        data = MetricsAttributes()
        data.attributes = results

        return data
