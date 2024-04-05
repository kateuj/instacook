from flask import render_template, request, redirect, url_for
from recipes import app, db
from recipes.models import Mealplans, Recipe


@app.route("/")
def index():
    return render_template("base.html")