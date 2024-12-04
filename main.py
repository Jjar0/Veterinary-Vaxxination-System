from datetime import datetime, timedelta

class Pet:  #Parent class for all animal classes
    def __init__(self, name, birthDate, lastVac):  #Initialize a pet object and info
        self.name = name
        self.birthDate = datetime.strptime(birthDate, "%Y/%m/%d")  #Convert time string into datetime using strptime
        self.lastVac = datetime.strptime(lastVac, "%Y/%m/%d")

    def getNext(self, startDate, days): #Add days to the given date using timedelta
        return startDate + timedelta(days=days)

    def getFutureDate(self, startDate, interval):
        today = datetime.now()
        futureDate = startDate

        while futureDate <= today: #Incrementally add intervals until future_date is strictly in the future
            futureDate = self.getNext(futureDate, interval)

        return futureDate


class Dog(Pet):  #Animal class for dogs
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Dog",
            "nextVac": self.getFutureDate(self.lastVac, 365).strftime("%Y/%m/%d"),
            "nextCheck": self.getFutureDate(self.birthDate, 365).strftime("%Y/%m/%d"),
        }


class Cat(Pet):  #Animal class for cats
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Cat",
            "nextVac": self.getFutureDate(self.lastVac, 180).strftime("%Y/%m/%d"),
            "nextCheck": self.getFutureDate(self.birthDate, 180).strftime("%Y/%m/%d"),
        }


class Rabbit(Pet):  #Animal class for rabbits
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Rabbit",
            "nextVac": self.getFutureDate(self.lastVac, 90).strftime("%Y/%m/%d"),
            "nextCheck": self.getFutureDate(self.birthDate, 180).strftime("%Y/%m/%d"),
        }


class Reptile(Pet):  #Animal class for reptiles
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Reptile",
            "nextVac": "N/A",  #No vaccination needed
            "nextCheck": self.getFutureDate(self.birthDate, 365).strftime("%Y/%m/%d"),
        }


class Bird(Pet):  #Animal class for birds
    def getSchedule(self):
        return {
            "name": self.name,
            "animal": "Bird",
            "nextVac": "N/A",  #No vaccination needed
            "nextCheck": self.getFutureDate(self.birthDate, 730).strftime("%Y/%m/%d"),
        }


def factory(name, animal, birthDate, lastVac):  #Factory function creates animal schedule profile
    animalDict = {  #Dictionary linking animal types to their class
        "DOG": Dog,
        "CAT": Cat,
        "RABBIT": Rabbit,
        "REPTILE": Reptile,
        "BIRD": Bird,
    }

    userPet = animalDict.get(animal.upper())  #Find the class based on the animal type using 'get'
    return userPet(name, birthDate, lastVac)


def menu():
    animalArray = ['DOG', 'CAT', 'RABBIT', 'REPTILE', 'BIRD']  #Array of all animals
    vaccineArray = ['DOG', 'CAT', 'RABBIT']  #Array of animals that need vaccines

    print("\n[Please enter pet information]\n")

    animal = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ").strip().upper()
    if animal not in animalArray:  #Validation to ensure listed animal is picked
        print("\nPlease enter an animal from the list presented.\n")
        menu()


    name = input("What is your pet's name?\n> ").strip()  #Pet name input

    birthDate = input("What is your pet's date of birth (YYYY/MM/DD)\n> ").strip()  #Request birth date
    try:
        datetime.strptime(birthDate, "%Y/%m/%d")  #Validate input format
    except ValueError:
        print("\nInvalid date format, Please use YYYY/MM/DD.")
        menu()


    if animal in vaccineArray:
        lastVac = input("When was your pet's last vaccination (YYYY/MM/DD)\n> ").strip()  #Request last vaccine date
        try:
            datetime.strptime(lastVac, "%Y/%m/%d")  #Validate input format
        except ValueError:
            print("\nInvalid date format, Please use YYYY/MM/DD.")
            menu()

    if animal not in vaccineArray:
        lastVac = ("2000/12/12").strip() #Placeholder date for non-vac animals

    pet = factory(name, animal, birthDate, lastVac)  #Create the pet object through the factory function
    schedule = pet.getSchedule()  #Get the pet's vaccination and health check schedule

    print("\nVaccination and Health Check Schedule:") #Output adjusted dates and information to user
    print(f"Name: {schedule['name']}")
    print(f"Animal: {schedule['animal']}")
    print(f"Next Vaccination: {schedule['nextVac']}")
    print(f"Next Health Check: {schedule['nextCheck']}")

    menu() #Start over :)

print("// Pet Vaccination and Health Checkup System //")
menu()
