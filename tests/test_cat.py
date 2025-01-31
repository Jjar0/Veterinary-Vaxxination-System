import unittest
from datetime import datetime
from models.cat import Cat

class TestCat(unittest.TestCase):

    def setUp(self):
        # Set up a Cat object for testing
        self.cat = Cat(name="Whiskers", birthDate="2019/06/15", lastVac="2023/06/15")

    def test_cat_initialization(self):
        # Test that a Cat object is correctly initialized
        self.assertEqual(self.cat.getSchedule()["name"], "Whiskers")
        self.assertEqual(self.cat.getSchedule()["animal"], "Cat")
        self.assertEqual(self.cat._vacInterval, 180)  # Cats need vaccination every 180 days
        self.assertEqual(self.cat._checkInterval, 180)  # Health check every 180 days

    def test_getNext(self):
        # Test if getNext correctly adds days to a date
        test_date = datetime(2023, 1, 1)
        expected_date = datetime(2023, 6, 30)  # 180 days later
        self.assertEqual(self.cat.getNext(test_date, 180), expected_date)

    def test_getFutureDate(self):
        # Test if getFutureDate correctly calculates the next vaccination date
        test_date = datetime(2019, 6, 15)
        interval = 180
        future_date = self.cat.getFutureDate(test_date, interval)
        self.assertTrue(future_date > datetime.now())  # Future date should be in the future

    def test_getSchedule(self):
        # Test if getSchedule returns a valid dictionary
        schedule = self.cat.getSchedule()
        self.assertIn("name", schedule)
        self.assertIn("animal", schedule)
        self.assertIn("nextVac", schedule)  
        self.assertIn("nextCheck", schedule)
        self.assertNotEqual(schedule["nextVac"], "N/A")  # Cats require vaccinations

if __name__ == "__main__":
    unittest.main()
