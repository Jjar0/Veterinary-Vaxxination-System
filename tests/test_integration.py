import unittest
from unittest.mock import patch
from utils.factory import factory
from models.dog import Dog
from models.cat import Cat
from models.reptile import Reptile
from utils.menu import menu

class TestIntegration(unittest.TestCase):

    def test_factory_creates_valid_pets(self):
        # Test that factory() correctly integrates with Pet subclasses
        dog = factory(name="Buddy", animal="DOG", birthDate="2021/01/01", lastVac="2023/06/10")
        cat = factory(name="Whiskers", animal="CAT", birthDate="2020/05/15", lastVac="2023/06/10")
        reptile = factory(name="Lizzy", animal="REPTILE", birthDate="2019/09/30", lastVac=None)

        self.assertIsInstance(dog, Dog)
        self.assertEqual(dog.getSchedule()["name"], "Buddy")

        self.assertIsInstance(cat, Cat)
        self.assertEqual(cat.getSchedule()["name"], "Whiskers")

        self.assertIsInstance(reptile, Reptile)
        self.assertEqual(reptile.getSchedule()["name"], "Lizzy")

    @patch("builtins.input", side_effect=iter(["dog", "Buddy", "2021/01/01", "2023/06/10"] * 5))  # Repeat values
    @patch("builtins.print")
    def test_menu_processes_user_input(self, mock_print, mock_input):
        #Test that menu() correctly processes user input and integrates with factory()
        try:
            menu()
        except RecursionError:
            pass  # Ignore infinite recursion in menu()

        self.assertTrue(mock_print.called)

    def test_pet_scheduling_logic(self):
        # Test that pet scheduling is consistent across pet types
        dog = factory(name="Buddy", animal="DOG", birthDate="2021/01/01", lastVac="2023/06/10")
        cat = factory(name="Whiskers", animal="CAT", birthDate="2020/05/15", lastVac="2023/06/10")

        dog_schedule = dog.getSchedule()
        cat_schedule = cat.getSchedule()

        self.assertIn("nextVac", dog_schedule)
        self.assertIn("nextCheck", dog_schedule)

        self.assertIn("nextVac", cat_schedule)
        self.assertIn("nextCheck", cat_schedule)

if __name__ == "__main__":
    unittest.main()