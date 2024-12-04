from datetime import datetime

class Pet:
    def __init__(self, name, birthDate, lastVac): #initialise a pet object and info
        self.name = name
        self.birthDate = datetime.strptime(birthDate, "%Y/%m/%d") #convert time string into datetime using striptime
        self.lastVac = datetime.strptime(lastVac, "%Y/%m/%d") #convert time string into datetime using striptime

    def getNext(self, date, days):

        year = date.year
        month = date.month
        day = date.day

        day += days 

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)): 
            days_in_month[1] = 29

        while day > days_in_month[month - 1]: 
            day -= days_in_month[month - 1]
            month += 1
            if month > 12:  
                month = 1
                year += 1

                if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    days_in_month[1] = 29
                else:
                    days_in_month[1] = 28

        return f"{year}/{month:02d}/{day:02d}"  #return formatted string

class Dog(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Dog",
            "nextVac": self.getNext(self.lastVac,365),
            "nextCheck": self.getNext(self.lastVac,365),
        }

class Cat(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Cat",
            "nextVac": self.getNext(self.lastVac,180),
            "nextCheck": self.getNext(self.lastVac,180),
        }

class Rabbit(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Rabbit",
            "nextVac": self.getNext(self.lastVac,90),
            "nextCheck": self.getNext(self.lastVac,180),
        }

class Reptile(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Reptile",
            "nextVac": "N/A",
            "nextCheck": self.getNext(self.lastVac,365),
        }

class Bird(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Bird",
            "nextVac": "N/A",
            "nextCheck": self.getNext(self.lastVac,730),
        }
    
def factory(name, animal, birthDate, lastVac): #factory function
    animalDict = { #dictionary linking animal types to their class
        "DOG": Dog,
        "CAT": Cat,
        "RABBIT": Rabbit,
        "REPTILE": Reptile,
        "BIRD": Bird,
    }
    
    userPet = animalDict.get(animal.upper())#find the class based on the animal type using 'get'
    return userPet(name, birthDate, lastVac)
    
def menu():

    animalArray = ['DOG','CAT','RABBIT','REPTILE','BIRD']
    vaccineArray = ['DOG','CAT','RABBIT']
    
    print("\n[Please enter pet information]\n")

    animal = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ").strip() #request input from user for pet species
    animal = animal.upper()
    if animal not in animalArray: #validation to ensure listed animal is picked
        print("Please enter an animal from the list presented.\n")
        menu()

    name = input("Whats is your pets name?\n>").strip() #pet name input

    birthDate = input("What is your pets date of birth (YYYY/MM/DD)\n> ").strip() #request birth date
    try:
        datetime.strptime(birthDate, "%Y/%m/%d") #checking input format against datetime format using striptime
    except:
        print("Invalid date format, Please use YYYY/MM/DD.")
        menu()

    if animal in vaccineArray:
        lastVac = input("When was your pets last vaccination (YYYY/MM/DD)\n> ").strip() #request last vaccine date
        try:
            datetime.strptime(lastVac, "%Y/%m/%d") #checking input format against datetime format using striptime
        except:
            print("Invalid date format, Please use YYYY/MM/DD.")
            menu()
    
    if animal not in vaccineArray:
        lastVac = ("2000/12/12").strip() #placeholder date

    pet = factory(name, animal, birthDate, lastVac)
    schedule = pet.getSchedule()

    print("\nVaccination and Health Check Schedule:")
    print(f"Name: {schedule['name']}")
    print(f"Animal: {schedule['animal']}")
    print(f"Next Vaccination: {schedule['nextVac']}")
    print(f"Next Health Check: {schedule['nextCheck']}")

print("// Pet Vaccination and Health Checkup System //")
menu()