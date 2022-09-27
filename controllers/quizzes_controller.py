from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import quizzes_repository

quizzes_blueprint = Blueprint("quizzes", __name__)

@quizzes_blueprint.route("/quizzes")
def index():
    country = quizzes_repository.random_country
    city = quizzes_repository.random_city
    sight = quizzes_repository.random_sight
    return render_template("quizzes/index.html", country=country,city=city,sight=sight)