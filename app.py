from flask import Flask, render_template
from controllers.sights_controller import sights_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint
from controllers.summary_controller import summary_blueprint
from controllers.quizzes_controller import quizzes_blueprint

app = Flask(__name__)

app.register_blueprint(sights_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(summary_blueprint)
app.register_blueprint(quizzes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)