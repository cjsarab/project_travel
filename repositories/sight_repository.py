from db.run_sql import run_sql

import repositories.city_repository as city_repository

from models.sight import Sight
from models.city import City

def save(sight):
    sql = "INSERT INTO sights (sight_name, is_visited, city_id) VALUES (%s, %s, %s) RETURNING *"
    values = [sight.sight_name, sight.is_visited, sight.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight

def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        sight = Sight(result['sight_name'], result['is_visited'], result['city_id'], result['id'])
    return sight

def select_all():
    sights = []
    sql = "SELECT * FROM sights"
    results = run_sql(sql)
    
    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['sight_name'], row['is_visited'], city, row['id'])
        sights.append(sight)
    return sights

def update(sight):
    sql = "UPDATE sights SET (sight_name, is_visited, city_id) = (%s, %s, %s) WHERE id = %s"
    values = [sight.sight_name, sight.is_visited, sight.city.id, sight.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

def select_city_by_sight(id):
    city = None
    sql = "SELECT city_id FROM sights WHERE id = %s"
    values = [id]
    city_id = run_sql(sql, values)[0]['city_id']

    if city_id:
        sql = "SELECT * FROM cities WHERE id = %s"
        values = [city_id]
        city = run_sql(sql, values)
        for row in city:
            city = City(row['city_name'], row['is_visited'], row['id'])
    return city

def total_visited_sights():
    sights = select_all()
    visited_sights = []
    for sight in sights:
        if sight.is_visited == True:
            visited_sights.append(sight)
    return visited_sights