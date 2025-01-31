from models.dog import Dog
from models.cat import Cat
from models.rabbit import Rabbit
from models.reptile import Reptile
from models.bird import Bird

def factory(name, animal, birthDate, lastVac=None):  # Factory function creates pet object
    animalDict = {  
        "DOG": Dog,
        "CAT": Cat,
        "RABBIT": Rabbit,
        "REPTILE": Reptile,
        "BIRD": Bird,
    }

    if animal in ['REPTILE', 'BIRD']:
        return animalDict[animal](name, birthDate)  # No lastVac required
    else:
        return animalDict[animal](name, birthDate, lastVac)  # Requires vaccination