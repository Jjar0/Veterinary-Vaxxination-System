from datetime import datetime
from utils.factory import factory

def menu():
    animalArray = ['DOG', 'CAT', 'RABBIT', 'REPTILE', 'BIRD']
    vaccineArray = ['DOG', 'CAT', 'RABBIT']

    print("\n[Please enter pet information]\n")

    while True:
        animal = input("What is your pet? (dog, cat, rabbit, reptile, bird) or type 'EXIT' to quit\n> ").strip().upper()

        if animal == "EXIT":
            print("\nExiting menu...")
            return  #Graceful exit

        if animal in animalArray:
            break  #exit loop
        else:
            print("\nPlease enter an animal from the list presented.")

    name = input("What is your pet's name?\n> ").strip()

    while True:
        birthDate = input("What is your pet's date of birth (YYYY/MM/DD)\n> ").strip()
        try:
            datetime.strptime(birthDate, "%Y/%m/%d")
            break  # ✅ Valid date, exit loop
        except ValueError:
            print("\nInvalid date format, please use YYYY/MM/DD.")

    lastVac = None
    if animal in vaccineArray:
        while True:
            lastVac = input("When was your pet's last vaccination (YYYY/MM/DD)\n> ").strip()
            try:
                datetime.strptime(lastVac, "%Y/%m/%d")
                break  # ✅ Valid date, exit loop
            except ValueError:
                print("\nInvalid date format, please use YYYY/MM/DD.")

    pet = factory(name, animal, birthDate, lastVac)
    schedule = pet.getSchedule()

    print("\nVaccination and Health Check Schedule:")
    print(f"Name: {schedule['name']}")
    print(f"Animal: {schedule['animal']}")
    print(f"Next Vaccination: {schedule['nextVac']}")
    print(f"Next Health Check: {schedule['nextCheck']}")

    input("\nPress 'Enter' to proceed or type 'EXIT' to quit.\n> ")

    return