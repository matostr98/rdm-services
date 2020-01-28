import json

from generator.random_entity import RandomEntity

with open('resources/test.json') as json_file:
    data = json.load(json_file)
    print(data)

    entities = data['attributes']

    print(entities)
