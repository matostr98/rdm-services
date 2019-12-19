class ProbabilityEntity:
    def __init__(self, value, weight: int):
        self.weight = weight

        self.value = value

    def __str__(self):
        return str(self.value) + " " + str(self.weight)



