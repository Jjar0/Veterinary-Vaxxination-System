from models.pet import Pet

class Cat(Pet):
    def __init__(self, name, birthDate, lastVac):
        super().__init__(name, birthDate, lastVac, vacInterval=180, checkInterval=180)