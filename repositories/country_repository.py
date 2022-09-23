from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries"