import unittest

from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("Paris", True, 1)

    def test_city_has_name(self):
        self.assertEqual ("Paris", self.city.city_name)

    def test_city_is_visited_true(self):
        self.assertEqual (True, self.city.is_visited)
    
    def test_city_is_visited_false(self):
        self.city = City("Berlin", False, 2)
        self.assertEqual (False, self.city.is_visited)        