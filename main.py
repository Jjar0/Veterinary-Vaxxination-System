from datetime import datetime

class Pet:
    def __init__(self, name, birthDate, lastVac):
        self.name = name

class Dog(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Dog",
            "nextVac": self.getNext(365),
            "nextCheck": self.getNext(365),
        }

class Cat(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Cat",
            "nextVac": self.getNext(180),
            "nextCheck": self.getNext(180),
        }

class Rabbit(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Rabbit",
            "nextVac": self.getNext(90),
            "nextCheck": self.getNext(180),
        }

class Reptile(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Reptile",
            "nextVac": self.getNext(0),
            "nextCheck": self.getNext(365),
        }

class Bird(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Bird",
            "nextVac": self.getNext(0),
            "nextCheck": self.getNext(730),
        }

def menu():

    animalArray = ['DOG','CAT','RABBIT','REPTILE','BIRD']
    
    print("\n[Please enter pet information]\n")

    animal = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ")
    animal = animal.upper()
    if animal not in animalArray:
        print("Please enter an animal from the list presented.\n")
        menu()

    name = input("Whats is your pets name?\n>")
    
    birthDate = input("What is your pets date of birth (YYYY/MM/DD)\n> ")
    try:
        datetime.strptime(birthDate, "%Y/%m/%d")
    except:
        print("Invalid date format, Please use YYYY/MM/DD.")
        menu()
    
    lastVac = input("When was your pets last vaccination (YYYY/MM/DD)\n> ")
    try:
        validDate = datetime.strptime(birthDate, "%Y/%m/%d")
    except:
        print("Invalid date format, Please use YYYY/MM/DD.")
        menu()


print("// Pet Vaccination and Health Checkup System //")
menu()