import random
from repositories import country_repository, city_repository, sight_repository

def random_country():
    country = random.choice(country_repository.select_all())
    return country

def random_city():
    city = random.choice(city_repository.select_all())
    return city

def random_sight():
    sight = random.sight(sight_repository.select_all())
    return sight
    
