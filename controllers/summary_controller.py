from http.client import USE_PROXY
from flask import Flask, render_template, Blueprint
from repositories import country_repository, city_repository, sight_repository 

summary_blueprint = Blueprint("summary", __name__)

@summary_blueprint.route("/summary")
def summary():
    total_countries = len(country_repository.select_all())
    total_cities = len(city_repository.select_all())
    total_sights = len(sight_repository.select_all())

    visited_countries = len(country_repository.total_visited_countries())
    visited_cities = len(city_repository.total_visited_cities())
    visited_sights = len(sight_repository.total_visited_sights())

    return render_template("summary/index.html", total_countries=total_countries, total_cities=total_cities, total_sights=total_sights, visited_countries=visited_countries, visited_cities=visited_cities,
    visited_sights=visited_sights)