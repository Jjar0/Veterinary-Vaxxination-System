from models.pet import Pet

class Reptile(Pet):
    def __init__(self, name, birthDate):
        super().__init__(name, birthDate, vacInterval=None, checkInterval=365)