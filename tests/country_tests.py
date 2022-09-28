import unittest

from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("France", True)

    def test_country_has_name(self):
        self.assertEqual("France", self.country.country_name)

    def test_country_is_visited(self):
        self.assertEqual(True, self.country.is_visited)
