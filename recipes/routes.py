from flask import render_template, request, redirect, url_for
from recipes import app, db
from recipes.models import User, Cookbook, Recipe


@app.route("/")
def home():
    return render_template("base.html")