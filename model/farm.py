class Farm:
    def __init__(self, place: str, count_of_animals: int, fan_power_wt: float):
        self.place = place
        self.count_of_animals = count_of_animals
        self.fan_power_wt = fan_power_wt

    def __str__(self):
        return self.place + " " + str(self.count_of_animals) + " " + str(self.fan_power_wt)