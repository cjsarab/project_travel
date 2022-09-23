from db.run_sql import run_sql

from models.country import Country

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