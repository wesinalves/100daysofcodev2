# Python Journey - Chapter 19
# Unit test for name function

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Tony Stark' work?"""
        formatted_name = get_formatted_name('tony', 'stark')
        self.assertEqual(formatted_name, 'Tony Stark')
    
    '''
    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'amadeus', 'mozart')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
    '''
    
unittest.main()