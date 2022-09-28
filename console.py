import pdb

from models.country import Country
from models.city import City
from models.sight import Sight

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

sight_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("France", True)
country_repository.save(country_1)
country_2 = Country("Germany", False)
country_repository.save(country_2)
country_3 = Country("Italy", True)
country_repository.save(country_3)

city_1 = City("Paris", True, country_1)
city_repository.save(city_1)
city_2 = City("Berlin", False, country_2)
city_repository.save(city_2)
city_3 = City("Rome", False, country_3)
city_repository.save(city_3)

sight_1 = Sight("Eiffel Tower", True, city_1)
sight_repository.save(sight_1)
sight_2 = Sight("Brandenburg Gate", False, city_2)
sight_repository.save(sight_2)
sight_3 = Sight("Trevi Fountain", False, city_3)
sight_repository.save(sight_3)

# country_repository.select_all()
# city_repository.select_all()
# sight_repository.select_all()


