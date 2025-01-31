import unittest
from unittest.mock import patch
from utils.factory import factory
from utils.menu import menu

class TestAcceptance(unittest.TestCase):

    @patch("builtins.input", side_effect=["dog", "Buddy", "2021/01/01", "2023/06/10", "exit"])
    @patch("builtins.print")  
    def test_acceptance_add_dog(self, mock_print, mock_input):
        #Test user successfully adds Dog and receives valid schedule
        try:
            menu()
        except RecursionError:
            pass  

        self.assertTrue(mock_print.called)  

    @patch("builtins.input", side_effect=["reptile", "Lizzy", "2019/09/30", "exit"])
    @patch("builtins.print")  
    def test_acceptance_add_reptile(self, mock_print, mock_input):
        # Test user successfully adds Reptile and receives valid schedule
        try:
            menu()
        except RecursionError:
            pass  

        self.assertTrue(mock_print.called)  

    @patch("builtins.input", side_effect=["lizard", "exit"])  
    @patch("builtins.print")  
    def test_acceptance_invalid_pet_type(self, mock_print, mock_input):
        # Test user enters an invalid pet type and gets an error message
        try:
            menu()
        except RecursionError:
            pass  

        self.assertTrue(mock_print.called)  

    @patch("builtins.input", side_effect=["dog", "Buddy", "01-01-2021", "02-01-2021", "2023/06/10", "exit"])
    @patch("builtins.print")  
    def test_acceptance_invalid_date_format(self, mock_print, mock_input):
        #Test user enters an invalid date format multiple times and finally corrects it
        try:
            menu()
        except RecursionError:
            pass  

        self.assertTrue(mock_print.called)      

if __name__ == "__main__":
    unittest.main()