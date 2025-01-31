import unittest
from datetime import datetime
from models.reptile import Reptile

class TestReptile(unittest.TestCase):

    def setUp(self):
        # Set up Reptile object for testing
        self.reptile = Reptile(name="Lizzy", birthDate="2018/07/15")

    def test_reptile_initialization(self):
        # Test Reptile object is correctly initialized
        self.assertEqual(self.reptile.getSchedule()["name"], "Lizzy")
        self.assertEqual(self.reptile.getSchedule()["animal"], "Reptile")
        self.assertIsNone(self.reptile._lastVac)  # Reptiles don't have vaccinations
        self.assertEqual(self.reptile._checkInterval, 365)  # Health check interval should be 365 days

    def test_getNext(self):
        # Test getNext correctly adds days to a date
        test_date = datetime(2023, 1, 1)
        expected_date = datetime(2024, 1, 1)  # 365 days later
        self.assertEqual(self.reptile.getNext(test_date, 365), expected_date)

    def test_getFutureDate(self):
        # Test getFutureDate correctly calculates next health check
        test_date = datetime(2018, 7, 15)
        interval = 365  # Reptile health check interval
        future_date = self.reptile.getFutureDate(test_date, interval)
        self.assertTrue(future_date > datetime.now())  # Future date should be in future

    def test_getSchedule(self):
        # Test getSchedule returns a valid dictionary
        schedule = self.reptile.getSchedule()
        self.assertIn("name", schedule)
        self.assertIn("animal", schedule)
        self.assertIn("nextVac", schedule)  # Should be N/A for reptiles
        self.assertIn("nextCheck", schedule)
        self.assertEqual(schedule["nextVac"], "N/A")  # Reptiles don't have vaccinations

if __name__ == "__main__":
    unittest.main()
