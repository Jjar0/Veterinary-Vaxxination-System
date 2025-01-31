from models.pet import Pet

class Rabbit(Pet):
    def __init__(self, name, birthDate, lastVac):
        super().__init__(name, birthDate, lastVac, vacInterval=90, checkInterval=180)