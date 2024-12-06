from datetime import datetime, timedelta

class Pet:  # Parent class for all animal classes
    def __init__(self, name, birthDate, lastVac=None, vacInterval=None, checkInterval=None):
        self.__name = name  # Private: Encapsulates the pet's name
        self.__birthDate = datetime.strptime(birthDate, "%Y/%m/%d")  # Private: Encapsulates birth date
        self._lastVac = datetime.strptime(lastVac, "%Y/%m/%d") if lastVac else None  # Protected: Encapsulates last vaccination date
        self._vacInterval = vacInterval  # Protected: Vaccination interval
        self._checkInterval = checkInterval  # Protected: Health check interval

    def getNext(self, startDate, days):  # Function adds days to the given date using timedelta
        return startDate + timedelta(days=days)

    def getFutureDate(self, startDate, interval):  # Function brings old dates into the present
        today = datetime.now()
        futureDate = startDate

        while futureDate <= today:  # Incrementally add intervals until future_date is strictly in the future
            futureDate = self.getNext(futureDate, interval)

        return futureDate

    def getSchedule(self):  # Handles vaccination schedule
        # Calls getFutureDate to find next vac if a vacdate is present
        nextVac = "N/A" if not self._lastVac else self.getFutureDate(self._lastVac, self._vacInterval).strftime("%Y/%m/%d")
        # Calls getFutureDate to find the next health check
        nextCheck = self.getFutureDate(self.__birthDate, self._checkInterval).strftime("%Y/%m/%d")

        return {
            "name": self.__name,
            "animal": self.__class__.__name__,
            "nextVac": nextVac,
            "nextCheck": nextCheck
        }

# Unique subclass which inherits from pet class and holds unique methods based on check/vac intervals
# Calls _init_ method from pet parent class using super()
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

def factory(name, animal, birthDate, lastVac):  # Factory function creates animal schedule profile
    animalDict = {  # Dictionary linking animal types to their class
        "DOG": Dog,
        "CAT": Cat,
        "RABBIT": Rabbit,
        "REPTILE": Reptile,
        "BIRD": Bird,
    }

    # For animals that don't need a vaccination, pass None for lastVac
    if animal in ['REPTILE', 'BIRD']:
        return animalDict[animal](name, birthDate)  # No lastVac required for Reptile or Bird
    else:
        return animalDict[animal](name, birthDate, lastVac)  # Animals requiring vaccination

def menu():
    animalArray = ['DOG', 'CAT', 'RABBIT', 'REPTILE', 'BIRD']  # Array of all animals
    vaccineArray = ['DOG', 'CAT', 'RABBIT']  # Array of animals that need vaccines

    print("\n[Please enter pet information]\n")

    animal = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ").strip()
    animal = animal.upper()
    if animal not in animalArray:  # Validation to ensure listed animal is picked
        print("\nPlease enter an animal from the list presented\n")
        menu()

    name = input("What is your pet's name?\n> ").strip()  # Pet name input

    birthDate = input("What is your pet's date of birth (YYYY/MM/DD)\n> ").strip()  # Request birth date
    try:
        datetime.strptime(birthDate, "%Y/%m/%d")  # Validate input format
    except:
        print("\nInvalid date format, please use YYYY/MM/DD")
        menu()

    lastVac = None  # Assign vaccine to none for animals which do not need them

    if animal in vaccineArray:
        lastVac = input("When was your pet's last vaccination (YYYY/MM/DD)\n> ").strip()  # Request last vaccine date
        try:
            datetime.strptime(lastVac, "%Y/%m/%d")
        except:
            print("\nInvalid date format, please use YYYY/MM/DD")
            menu()

    pet = factory(name, animal, birthDate, lastVac)  # Uses the factory function to create the pet object
    schedule = pet.getSchedule()  # Creates schedule from returned values

    print("\nVaccination and Health Check Schedule:")  # Output returned info to user
    print(f"Name: {schedule['name']}")
    print(f"Animal: {schedule['animal']}")
    print(f"Next Vaccination: {schedule['nextVac']}")
    print(f"Next Health Check: {schedule['nextCheck']}")

    input("\nPress 'Enter' to proceed\n>")  # Give option to proceed
    menu()

print("// Pet Vaccination and Health Checkup System //")
menu()