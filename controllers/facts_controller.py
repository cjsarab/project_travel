from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import country_repository, city_repository, sight_repository 

facts_blueprint = Blueprint("facts", __name__)

@facts_blueprint.route("/facts")
def facts():
    total_countries = len(country_repository.select_all())
    total_cities = len(city_repository.select_all())
    total_sights = len(sight_repository.select_all())

    # most_cities = country_repository.find_country_with_most_cities()
    # most_sights = city_repository.find_city_with_most_sights()

    visited_countries = len(country_repository.total_visited_countries())
    visited_cities = len(city_repository.total_visited_cities())
    visited_sights = len(sight_repository.total_visited_sights())

    return render_template("facts/index.html", total_countries=total_countries, total_cities=total_cities, total_sights=total_sights, visited_countries=visited_countries, visited_cities=visited_cities,
    visited_sights=visited_sights)