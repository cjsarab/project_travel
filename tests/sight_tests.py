import unittest

from models.sight import Sight

class TestSight(unittest.TestCase):
    def setUp(self):
        self.sight = Sight("Eiffel Tower", True, 1)

    def test_sight_has_name(self):
        self.assertEqual ("Eiffel Tower", self.sight.sight_name)

    def test_sight_is_visited_true(self):
        self.assertEqual (True, self.sight.is_visited)
    
    def test_sight_is_visited_false(self):
        self.sight = Sight("Brandenburg Gate", False, 2)
        self.assertEqual (False, self.sight.is_visited)