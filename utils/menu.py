from datetime import datetime
from utils.factory import factory
print("DEBUG: datetime module loaded successfully.", datetime)

def menu():
    animalArray = ['DOG', 'CAT', 'RABBIT', 'REPTILE', 'BIRD']
    vaccineArray = ['DOG', 'CAT', 'RABBIT']

    print("\n[Please enter pet information]\n")

    animal = input("What is your pet? (dog, cat, rabbit, reptile, bird)\n> ").strip().upper()
    if animal not in animalArray:
        print("\nPlease enter an animal from the list presented\n")
        return menu()

    name = input("What is your pet's name?\n> ").strip()

    birthDate = input("What is your pet's date of birth (YYYY/MM/DD)\n> ").strip()
    try:
        datetime.strptime(birthDate, "%Y/%m/%d")
    except ValueError:
        print("\nInvalid date format, please use YYYY/MM/DD")
        return menu()

    lastVac = None
    if animal in vaccineArray:
        lastVac = input("When was your pet's last vaccination (YYYY/MM/DD)\n> ").strip()
        try:
            datetime.strptime(lastVac, "%Y/%m/%d")
        except ValueError:
            print("\nInvalid date format, please use YYYY/MM/DD")
            return menu()

    pet = factory(name, animal, birthDate, lastVac)
    schedule = pet.getSchedule()

    print("\nVaccination and Health Check Schedule:")
    print(f"Name: {schedule['name']}")
    print(f"Animal: {schedule['animal']}")
    print(f"Next Vaccination: {schedule['nextVac']}")
    print(f"Next Health Check: {schedule['nextCheck']}")

    input("\nPress 'Enter' to proceed\n>")
    menu()