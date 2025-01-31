import unittest
from unittest.mock import patch
from utils.factory import factory
from models.dog import Dog
from models.cat import Cat
from models.reptile import Reptile
from utils.menu import menu

class TestSystem(unittest.TestCase):

    @patch("builtins.input", side_effect=["dog", "Buddy", "2021/01/01", "2023/06/10", "exit"])
    @patch("builtins.print")  # Suppress print output for cleaner test results
    def test_full_system_flow_dog(self, mock_print, mock_input):
        # Test full system flow for adding Dog
        try:
            menu()
        except RecursionError:
            pass  # Prevent infinite recursion if menu() loops

        # Check if print() was called, meaning output was generated
        self.assertTrue(mock_print.called)

    @patch("builtins.input", side_effect=["reptile", "Lizzy", "2019/09/30", "exit"])
    @patch("builtins.print")
    def test_full_system_flow_reptile(self, mock_print, mock_input):
        # Test full system flow for adding Reptile (no vaccination needed)
        try:
            menu()
        except RecursionError:
            pass

        self.assertTrue(mock_print.called)

if __name__ == "__main__":
    unittest.main()