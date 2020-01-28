import json

from attributes.models import MetricsAttributes


class AttributesService:
    def __init__(self, sourcefile):
        with open(sourcefile) as json_file:
            data = json.load(json_file)
            self.entities = data['attributes']

    def generate_attributes(self):
        results_list = []

        for e in self.entities:
            result = \
                {
                    'key': e['key'],
                    'value': e['value']
                }
            results_list.append(result)
        data = MetricsAttributes()
        data.attributes = results_list
        return data
