from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint

quizzes_blueprint = Blueprint("quizzes", __name__)

@quizzes_blueprint.route("/quizzes")
def quizzes():
    return render_template("quizzes/index.html")