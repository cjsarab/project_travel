from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import city_repository, sight_repository
from models.sight import Sight

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", all_sights = sights)

@sights_blueprint.route("/sights/new/<id>")
def new_sight_by_city(id):
    city = city_repository.select(id)
    return render_template("/sights/new.html", city=city)

@sights_blueprint.route("/sights", methods = ['POST'])
def create_sight():
    sight_name = request.form['sight_name']
    is_visited = request.form['is_visited']
    city_id = request.form['city_id']
    city = city_repository.select(city_id)
    new_sight = Sight(sight_name, is_visited, city)
    sight_repository.save(new_sight)
    return redirect ('/sights')

@sights_blueprint.route("/sights/<id>")
def show_sight(id):
    sight = sight_repository.select(id)
    city = sight_repository.select_city_by_sight(id)
    return render_template("sights/show.html", sight=sight, city=city)

@sights_blueprint.route("/sights/<id>/edit")
def edit_sight(id):
    sight = sight_repository.select(id)
    cities = city_repository.select_all()
    return render_template('sights/edit.html', sight = sight, all_cities = cities)

@sights_blueprint.route("/sights/<id>", methods=['POST'])
def update_sight(id):
    sight_name = request.form['sight_name']
    is_visited = request.form['is_visited']
    city_id = request.form['city_id']
    city = city_repository.select(city_id)

    sight_to_update = Sight(sight_name, is_visited, city, id)
    sight_repository.update(sight_to_update)
    return redirect ('/sights/' + id)

@sights_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sight(id):
    sight_to_delete = id
    sight_repository.delete(sight_to_delete)
    return redirect ('/sights')