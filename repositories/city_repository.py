from db.run_sql import run_sql

import repositories.country_repository as country_repository

from models.sight import Sight
from models.city import City
from models.country import Country
import pdb

def save(city):
    sql = "INSERT INTO cities (city_name, is_visited, country_id) VALUES (%s, %s, %s) RETURNING *"
    values = [city.city_name, city.is_visited, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        city = City(result['city_name'], result['is_visited'], result['country_id'], result['id'])
    return city

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    
    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], row['is_visited'], country, row['id'])
        cities.append(city)
    return cities

def update(city):
    sql = "UPDATE cities SET (city_name, is_visited, country_id) = (%s, %s, %s) WHERE id = %s"
    values = [city.city_name, city.is_visited, city.country.id, city.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def select_country_by_city(id):
    country = None
    sql = "SELECT country_id FROM cities WHERE id = %s"
    values = [id]
    country_id = run_sql(sql, values)[0]['country_id']

    if country_id:
        sql = "SELECT * FROM countries WHERE id = %s"
        values = [country_id]
        country = run_sql(sql, values)
        for row in country:
            country = Country(row['country_name'], row['is_visited'], row['id'])
    return country

def select_all_sights_from_city(id):
    sights = []
    sql = "SELECT * FROM sights WHERE city_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        city = select(row['city_id'])
        sight = Sight(row['sight_name'], row['is_visited'], city, row['id'])
        sights.append(sight)
    return sights