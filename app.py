from flask import Flask, render_template, request

import random

random_number = random.randint(1, 99)

app = Flask(__name__)

# Create required routes
# Home route
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# Route to choose number
@app.route("/game", methods=['GET'])
def game_first():
    return render_template("game.html", random_number=random_number)

# Compare number chosen by user to random number and return appropriate page
@app.route("/guess/<int:number_chosen>", methods=['GET'])
def game(number_chosen):
    if number_chosen < random_number:
        return render_template("low.html", number_chosen=number_chosen)
    elif number_chosen > random_number:
        return render_template("high.html", number_chosen=number_chosen)
    elif number_chosen == random_number:
        return render_template("correct_number.html", number_chosen=number_chosen, random_number=random_number)