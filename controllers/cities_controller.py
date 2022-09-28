from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import country_repository, city_repository
from models.city import City

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

@cities_blueprint.route("/cities/new/<id>")
def new_city_by_country(id):
    country = country_repository.select(id)
    return render_template("/cities/new.html", country=country)

@cities_blueprint.route("/cities", methods = ['POST'])
def create_city():
    city_name = request.form['city_name']
    is_visited = request.form['is_visited']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    new_city = City(city_name, is_visited, country)
    city_repository.save(new_city)
    return redirect ('/cities')

@cities_blueprint.route("/cities/<id>")
def show_city(id):
    city = city_repository.select(id)
    country = city_repository.select_country_by_city(id)
    sights = city_repository.select_all_sights_from_city(id)
    city_repository.set_city_visited_true_if_sight_visited_true(id)
    return render_template("cities/show.html", city=city, country=country, sights=sights)

@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city = city, all_countries = countries)

@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    city_name = request.form['city_name']
    is_visited = request.form['is_visited']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)

    city_to_update = City(city_name, is_visited, country, id)
    city_repository.update(city_to_update)
    return redirect ('/cities/' + id)

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_to_delete = id
    city_repository.delete(city_to_delete)
    return redirect ('/cities')