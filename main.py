from datetime import datetime

class Pet:
    def __init__(self, name, birthDate, lastVac):
        self.name = name

class Dog(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Dog",
        }

class Cat(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Cat",
        }

class Rabbit(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Rabbit",
        }

class Reptile(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Reptile",
        }

class Bird(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Bird",
        }

