import unittest
from utils.factory import factory
from models.dog import Dog
from models.reptile import Reptile

class TestFactory(unittest.TestCase):

    def test_create_dog(self):
        # Test that the factory correctly creates a Dog object
        pet = factory(name="Rex", animal="DOG", birthDate="2021/05/15", lastVac="2023/06/10")
        self.assertIsInstance(pet, Dog)
        self.assertEqual(pet.getSchedule()["name"], "Rex")

    def test_create_reptile(self):
        # Test that the factory correctly creates a Reptile object
        pet = factory(name="Lizzy", animal="REPTILE", birthDate="2020/09/30")
        self.assertIsInstance(pet, Reptile)
        self.assertEqual(pet.getSchedule()["name"], "Lizzy")

if __name__ == "__main__":
    unittest.main()
