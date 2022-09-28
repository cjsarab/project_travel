import unittest

from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("France", True)

    def test_country_has_name(self):
        self.assertEqual("France", self.country.country_name)

    def test_country_is_visited_true(self):
        self.assertEqual(True, self.country.is_visited)
    
    def test_country_is_visited_false(self):
        self.country = Country("Germany", False, 2)
        self.assertEqual(False, self.country.is_visited)