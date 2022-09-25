from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import country_repository
from models.country import Country


countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("/countries/new.html")

@countries_blueprint.route("/countries", methods = ['POST'])
def create_country():
    country_name = request.form['country_name']
    is_visited = request.form['is_visited']

    new_country = Country(country_name, is_visited)
    country_repository.save(new_country)
    return redirect ('/countries')

@countries_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    return render_template("countries/show.html", country = country)

@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country = country)

@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    country_name = request.form['country_name']
    is_visited = request.form['is_visited']

    country_to_update = Country(country_name, is_visited, id)
    country_repository.update(country_to_update)
    return redirect ('/countries/' + id)

@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_to_delete = id
    country_repository.delete(country_to_delete)
    return redirect ('/countries')