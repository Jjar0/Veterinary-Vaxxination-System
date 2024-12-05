from datetime import datetime, timedelta

class Pet: #Parent class for all animal classes
    def __init__(self, name, birthDate, lastVac=None, vacInterval=None, checkInterval=None): #Initialize a pet object and info
        self.name = name
        self.birthDate = datetime.strptime(birthDate, "%Y/%m/%d") #Convert time string into datetime using strptime
        self.lastVac = datetime.strptime(lastVac, "%Y/%m/%d") if lastVac else None
        self.vac_interval = vacInterval  #Vaccination interval
        self.check_interval = checkInterval  #Health check interval

    def getNext(self, startDate, days): #Function adds days to the given date using timedelta
        return startDate + timedelta(days=days)

    def getFutureDate(self, startDate, interval): #Function brings old dates into the present 
        today = datetime.now()
        futureDate = startDate

        while futureDate <= today: #Incrementally add intervals until future_date is strictly in the future
            futureDate = self.getNext(futureDate, interval)

        return futureDate

    def getSchedule(self): #Handles vaccination schedule
        
        nextVac = "N/A" if not self.lastVac else self.getFutureDate(self.lastVac, self.vacInterval).strftime("%Y/%m/%d")
        nextCheck = self.getFutureDate(self.birthDate, self.checkInterval).strftime("%Y/%m/%d")

        return {
            "name": self.name,
            "animal": self.__class__.__name__,
            "nextVac": nextVac,
            "nextCheck": nextCheck
        }

#Unique subclass which inherits from pet class and hold unique methods based on check/vac intervals

class Dog(Pet):
    def __init__(self, name, birthDate, lastVac):
        super().__init__(name, birthDate, lastVac, vacInterval=365, checkInterval=365)

class Cat(Pet):
    def __init__(self, name, birthDate, lastVac):
        super().__init__(name, birthDate, lastVac, vacInterval=180, checkInterval=180)

class Rabbit(Pet):
    def __init__(self, name, birthDate, lastVac):
        super().__init__(name, birthDate, lastVac, vacInterval=90, checkInterval=180)

class Reptile(Pet):
    def __init__(self, name, birthDate):
        super().__init__(name, birthDate, vacInterval=None, checkInterval=365)

class Bird(Pet):
    def __init__(self, name, birthDate):
        super().__init__(name, birthDate, vacInterval=None, checkInterval=730)

def factory(name, animal, birthDate, lastVac): #Factory function creates animal schedule profile
    animalDict = { #Dictionary linking animal types to their class
        "DOG": Dog,
        "CAT": Cat,
        "RABBIT": Rabbit,
        "REPTILE": Reptile,
        "BIRD": Bird,
    }

    userPet = animalDict.get(animal) #Find the class based on the animal type using 'get'
    return userPet(name, birthDate, lastVac) if lastVac else userPet(name, birthDate)

def menu():
    animalArray = ['DOG', 'CAT', 'RABBIT', 'REPTILE', 'BIRD'] #Array of all animals
    vaccineArray = ['DOG', 'CAT', 'RABBIT'] #Array of animals that need vaccines


    print("\n[Please enter pet information]\n")

    animal = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ").strip()
    animal = animal.upper()
    if animal not in animalArray: #Validation to ensure listed animal is picked
        print("\nPlease enter an animal from the list presented\n")
        menu()

    name = input("What is your pet's name?\n> ").strip() #Pet name input

    birthDate = input("What is your pet's date of birth (YYYY/MM/DD)\n> ").strip() #Request birth date
    try:
        datetime.strptime(birthDate, "%Y/%m/%d") #Validate input format
    except:
        print("\nInvalid date format, please use YYYY/MM/DD")
        menu()

    lastVac = None #Assign vaccine to none for naimals which do not need them

    if animal in vaccineArray:
        lastVac = input("When was your pet's last vaccination (YYYY/MM/DD)\n> ").strip() #Request last vaccine date
        try:
            datetime.strptime(lastVac, "%Y/%m/%d")
        except:
            print("\nInvalid date format, please use YYYY/MM/DD")
            menu()

    pet = factory(name, animal, birthDate, lastVac) #Uses the factory function to create the pets schedule and displays the results
    schedule = pet.getSchedule()

    print("\nVaccination and Health Check Schedule:")
    print(f"Name: {schedule['name']}")
    print(f"Animal: {schedule['animal']}")
    print(f"Next Vaccination: {schedule['nextVac']}")
    print(f"Next Health Check: {schedule['nextCheck']}")

    input("\nPress 'Enter' to proceed/n>") #give option to proceed
    menu()

print("// Pet Vaccination and Health Checkup System //")
menu()