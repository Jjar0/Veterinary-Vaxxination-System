from datetime import datetime

class Pet:
    def __init__(self, name, birthDate, lastVac):
        self.name = name

class Dog(Pet):
    def get_schedule(self):
        return {
            "name": self.name,
            "type": "Dog",
        }
