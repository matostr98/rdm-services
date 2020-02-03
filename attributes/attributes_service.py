import json
import random

from attributes.models import MetricsAttributes


def generate_values_from_array(array, count=1, weights=None):
    value = random.choices(array, weights=weights, k=count)
    if len(value) == 1:
        value = value[0]
    return value


def generate_values_from_range(maximum, minimum=0, count=1, num_type='int', floating_points=None):
    value = 0
    if num_type == 'int':
        value = random.choices(range(minimum, maximum), k=count)
    elif num_type == 'float':
        value = []
        for i in range(count):
            v = random.random() * (maximum - minimum) + minimum
            value.append(v)

    if floating_points is not None:
        for i in range(len(value)):
            value[i] = round(value[i], floating_points)

    if len(value) == 1:
        value = value[0]

    return value


class AttributesService:
    def __init__(self, sourcefile):
        with open(sourcefile) as json_file:
            data = json.load(json_file)
            self.entities = data['model']

    def generate_attributes(self):
        results = {}

        for e in self.entities:
            if 'count' in e:
                if 'maximum' in e:
                    if 'minimum' in e:
                        if 'type' in e:
                            if 'floating_points' in e:
                                results[e['key']] = generate_values_from_range(e['maximum'], minimum=e['minimum'],
                                                                               count=e['count'], num_type=e['type'],
                                                                               floating_points=e['floating_points'])
                            else:
                                results[e['key']] = generate_values_from_range(e['maximum'], minimum=e['minimum'],
                                                                               count=e['count'], num_type=e['type'])
                        else:
                            results[e['key']] = generate_values_from_range(e['maximum'], minimum=e['minimum'],
                                                                           count=e['count'])
                    elif 'type' in e:
                        if 'floating_points' in e:
                            results[e['key']] = generate_values_from_range(e['maximum'],
                                                                           count=e['count'], num_type=e['type'],
                                                                           floating_points=e['floating_points'])
                        else:
                            results[e['key']] = generate_values_from_range(e['maximum'],
                                                                           count=e['count'], num_type=e['type'])
                    else:
                        results[e['key']] = generate_values_from_range(e['maximum'],
                                                                       count=e['count'])

                elif 'weights' in e:
                    results[e['key']] = generate_values_from_array(e['array'], weights=e['weights'], count=e['count'])
                else:
                    results[e['key']] = generate_values_from_array(e['array'], count=e['count'])

            elif 'maximum' in e:
                if 'minimum' in e:
                    if 'type' in e:
                        if 'floating_points' in e:
                            results[e['key']] = generate_values_from_range(e['maximum'], minimum=e['minimum'],
                                                                           num_type=e['type'],
                                                                           floating_points=e['floating_points'])
                        else:
                            results[e['key']] = generate_values_from_range(e['maximum'], minimum=e['minimum'],
                                                                           num_type=e['type'])
                    else:
                        results[e['key']] = generate_values_from_range(e['maximum'], minimum=e['minimum'])
                elif 'type' in e:
                    if 'floating_points' in e:
                        results[e['key']] = generate_values_from_range(e['maximum'],
                                                                       num_type=e['type'],
                                                                       floating_points=e['floating_points'])
                    else:
                        results[e['key']] = generate_values_from_range(e['maximum'],
                                                                       num_type=e['type'])
                else:
                    results[e['key']] = generate_values_from_range(e['maximum'])

            elif 'weights' in e:
                results[e['key']] = generate_values_from_array(e['array'], weights=e['weights'])
            else:
                results[e['key']] = generate_values_from_array(e['array'])

        data = MetricsAttributes()
        data.attributes = results
        return data
