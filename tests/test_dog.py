import unittest
from models.dog import Dog

class TestDog(unittest.TestCase):

    def setUp(self):
        # Set up a Dog object
        self.dog = Dog(name="Buddy", birthDate="2020/01/01", lastVac="2023/01/01")

    def test_vaccination_interval(self):
        # Check that the dog's vaccination interval is set correctly
        self.assertEqual(self.dog._vacInterval, 365)

    def test_health_check_interval(self):
        # Check that the dog's health check interval is set correctly
        self.assertEqual(self.dog._checkInterval, 365)

if __name__ == "__main__":
    unittest.main()
