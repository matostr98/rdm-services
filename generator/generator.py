from datetime import datetime
from random import randrange
from datetime import timedelta
import random

from generator.random_entity import RandomEntity


class Generator:
    def generate(self, entity: RandomEntity):
        result = []
        generated = self.__generate_with_wages(entity)

        for g in generated:
            result.append(g.value)

        return result

    def __generate_with_wages(self, entity: RandomEntity):
        print(entity.values)
        print(entity.weights)
        print(entity.count)
        values = random.choices(entity.values, weights=entity.weights, k=entity.count)

        # flat_values = []
        # for v in values:
        #     flat_values.append(v)

        return values

    def __generate_in_range(self, min_value: int, max_value: int):
        value = random.randint(min_value, max_value)
        return value

    def __generate_from_set(self, set_of_values: []):
        value = random.choice(set_of_values)
        return value

    def __generate_random_date(self, min_date, max_date):
        """
        This function will return a random datetime between two dates
        as strings
        """

        date_start = datetime.strptime(min_date, '%m/%d/%Y %I:%M %p')
        date_end = datetime.strptime(max_date, '%m/%d/%Y %I:%M %p')
        self.__generate_random_date_between(date_start, date_end)

    def __generate_random_date_between(self, start, end):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
