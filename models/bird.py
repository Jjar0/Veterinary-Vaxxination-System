from models.pet import Pet

class Bird(Pet):
    def __init__(self, name, birthDate):
        super().__init__(name, birthDate, vacInterval=None, checkInterval=730)