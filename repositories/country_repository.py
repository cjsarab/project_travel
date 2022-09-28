from db.run_sql import run_sql

from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries (country_name, is_visited) VALUES (%s, %s) RETURNING *"
    values = [country.country_name, country.is_visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = Country(result['country_name'], result['is_visited'], result['id'])
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country_name'], row['is_visited'], row['id'])
        countries.append(country)
    return countries

def update(country):
    sql = "UPDATE countries SET (country_name, is_visited) = (%s, %s) WHERE id = %s"
    values = [country.country_name, country.is_visited, country.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def select_all_cities_from_country(id):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        country = select(row['country_id'])
        city = City(row['city_name'], row['is_visited'], country, row['id'])
        cities.append(city)
    return cities

def set_country_visited_true_if_city_visited_true(id):
    cities = select_all_cities_from_country(id)
    for city in cities:
        if city.is_visited:
            sql = "UPDATE countries SET is_visited = %s WHERE id = %s"
            values = [True, id]
            run_sql(sql, values)

def total_visited_countries():
    countries = select_all()
    visited_countries = []
    for country in countries:
        if country.is_visited == True:
            visited_countries.append(country)
    return visited_countries
