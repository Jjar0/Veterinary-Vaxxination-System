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
    
if __name__ == "__main__":
    pet_name = input("Enter pet's name\n>")
    pet_type = input("Enter pet's type (dog)\n> ")

    print(f"Name: {pet_name}")
    print(f"Type: {pet_type}")

