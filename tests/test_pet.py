import unittest
from datetime import datetime
from models.pet import Pet

class TestPet(unittest.TestCase):

    def setUp(self):
        # Set up pet object for testing
        self.pet = Pet(name="Fluffy", birthDate="2020/01/01", lastVac="2023/01/01", vacInterval=365, checkInterval=180)

    def test_getNext(self):
        # Test getNext correctly adds days to a date
        test_date = datetime(2023, 1, 1)
        expected = datetime(2024, 1, 1)
        self.assertEqual(self.pet.getNext(test_date, 365), expected)

    def test_getFutureDate(self):
        # Test if getFutureDate correctly calculates the next appointment
        test_date = datetime(2020, 1, 1)
        interval = 180
        expected_date = self.pet.getFutureDate(test_date, interval)  # What the function should return
        self.assertEqual(expected_date, self.pet.getNext(test_date, interval)) # validation of date acuraccy

    def test_getSchedule(self):
        # Test getSchedule returns correct data structure
        schedule = self.pet.getSchedule()
        self.assertEqual(schedule["name"], "Fluffy")
        self.assertEqual(schedule["animal"], "Pet")
        self.assertIn("nextVac", schedule)
        self.assertIn("nextCheck", schedule)

if __name__ == "__main__":
    unittest.main()
