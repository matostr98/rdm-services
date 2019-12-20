from generator.probability_entity import ProbabilityEntity
from generator.random_entity import RandomEntity
from generator.generator import Generator

banana = ProbabilityEntity(None, 1)
apple = ProbabilityEntity("apple", 1)
pear = ProbabilityEntity("pear", 0)
strawberry = ProbabilityEntity("strawberry", 1)
melon = ProbabilityEntity("melon", 1)

entity = RandomEntity("Fruit", 20, [banana, apple, pear, strawberry, melon])

generator = Generator()
result = generator.generate(entity)
print(result)



