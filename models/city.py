from operator import is_


class City:
    def __init__(self, city_name, is_visited, country, id=None):
        self.city_name = city_name
        self.is_visited = is_visited
        self.country = country
        self.id = id