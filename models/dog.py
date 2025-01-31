from models.pet import Pet

class Dog(Pet):
    def __init__(self, name, birthDate, lastVac):
        super().__init__(name, birthDate, lastVac, vacInterval=365, checkInterval=365)