import datetime

typeArray = [Dog,Cat,Rabbit,Reptile,Bird]

class Pet:
    def __init__(self, name, birthDate, lastVac):
        self.name = name

class Dog(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Dog",
            "nextVac": self.getNext(365),
            "nextCheck": self.getNext(365),
        }

class Cat(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Cat",
            "nextVac": self.getNext(180),
            "nextCheck": self.getNext(180),
        }

class Rabbit(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Rabbit",
            "nextVac": self.getNext(90),
            "nextCheck": self.getNext(180),
        }

class Reptile(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Reptile",
            "nextVac": self.getNext(0),
            "nextCheck": self.getNext(365),
        }

class Bird(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "type": "Bird",
            "nextVac": self.getNext(0),
            "nextCheck": self.getNext(730),
        }

while True:
    print("// Pet Vaccination and Health Checkup System //\n")

    type = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ")
    name = input("Whats is your pets name?\n>")
    birthDate = input("What is your pets date of birth (YYYY/MM/DD)\n> ")
    lastVac = input("When was your pets last vaccination (YYYY/MM/DD)\n> ")