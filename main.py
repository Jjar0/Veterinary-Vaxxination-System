from datetime import datetime, timedelta

class Pet:  # Parent class for all animal classes
    def __init__(self, name, birthDate, lastVac):  # Initialize a pet object and info
        self.name = name
        self.birthDate = datetime.strptime(birthDate, "%Y/%m/%d")  # Convert time string into datetime using strptime
        self.lastVac = datetime.strptime(lastVac, "%Y/%m/%d")

    def getNext(self, date, days):
        return date + timedelta(days=days)  #add days to the given date using timedelta

    def getFutureDate(self, startDate, interval): #function to to take entered dates and iterate themselves until present is reached
        today = datetime.now()
        nextDate = self.getNext(startDate, interval)

        while nextDate <= today: #loop until the calculated next date is in the future
            nextDate = self.getNext(nextDate, interval)

        return nextDate  #return as datetime object (to be formatted later)


class Dog(Pet):  #animal class which holds unique information about the species (checkup and vac times)
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Dog",
            "nextVac": self.getFutureDate(self.lastVac, 365).strftime("%Y/%m/%d"),
            "nextCheck": self.getFutureDate(self.birthDate, 365).strftime("%Y/%m/%d"),
        }


class Cat(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Cat",
            "nextVac": self.getFutureDate(self.lastVac, 180).strftime("%Y/%m/%d"),
            "nextCheck": self.getFutureDate(self.birthDate, 180).strftime("%Y/%m/%d"),
        }


class Rabbit(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Rabbit",
            "nextVac": self.getFutureDate(self.lastVac, 90).strftime("%Y/%m/%d"),
            "nextCheck": self.getFutureDate(self.birthDate, 180).strftime("%Y/%m/%d"),
        }


class Reptile(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Reptile",
            "nextVac": "N/A",
            "nextCheck": self.getFutureDate(self.birthDate, 365).strftime("%Y/%m/%d"),
        }


class Bird(Pet):
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Bird",
            "nextVac": "N/A",
            "nextCheck": self.getFutureDate(self.birthDate, 730).strftime("%Y/%m/%d"),
        }


def factory(name, animal, birthDate, lastVac):  #factory function creates animal schedule profile
    animalDict = {  #dictionary linking animal types to their class
        "DOG": Dog,
        "CAT": Cat,
        "RABBIT": Rabbit,
        "REPTILE": Reptile,
        "BIRD": Bird,
    }

    userPet = animalDict.get(animal.upper())  #find the class based on the animal type using 'get'
    return userPet(name, birthDate, lastVac)


def menu():
    animalArray = ['DOG', 'CAT', 'RABBIT', 'REPTILE', 'BIRD']  #array of all animals
    vaccineArray = ['DOG', 'CAT', 'RABBIT']  #array of animals that need vaccines

    print("\n[Please enter pet information]\n")

    animal = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ").strip().upper()
    if animal not in animalArray:  #validation to ensure listed animal is picked
        print("\nPlease enter an animal from the list presented.\n")
        menu()

    name = input("What is your pet's name?\n> ").strip()  #pet name input

    birthDate = input("What is your pet's date of birth (YYYY/MM/DD)\n> ").strip()  #request birth date
    try:
        datetime.strptime(birthDate, "%Y/%m/%d")  #validate input format
    except:
        print("\nInvalid date format, Please use YYYY/MM/DD.")
        menu()

    if animal in vaccineArray:
        lastVac = input("When was your pet's last vaccination (YYYY/MM/DD)\n> ").strip()  #request last vaccine date
        try:
            datetime.strptime(lastVac, "%Y/%m/%d")  #validate input format
        except:
            print("\nInvalid date format, Please use YYYY/MM/DD.")
            menu()
    
    if animal not in vaccineArray:
        lastVac == ("2000/01/01").strip()  #placeholder for animals that don't need vaccination

    pet = factory(name, animal, birthDate, lastVac)  #create the pet object through calling the factory function
    schedule = pet.getSchedule()  #get the pet's vaccination and health check schedule

    print("\nVaccination and Health Check Schedule:")
    print(f"Name: {schedule['name']}")
    print(f"Animal: {schedule['animal']}")
    print(f"Next Vaccination: {schedule['nextVac']}")
    print(f"Next Health Check: {schedule['nextCheck']}")


print("// Pet Vaccination and Health Checkup System //")
menu()