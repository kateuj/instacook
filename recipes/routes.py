from flask import render_template, request, redirect, url_for
from recipes import app, db
from recipes.models import Users, Cookbook, Recipe


@app.route("/")
def home():
    return render_template("base.html")

#register required
# sign out required
# delete account required

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/search")
def search():
    return render_template("search.html")


#@app.route("/shopping-list")
#def shoppingList():
#    return render_template("shopping-list.html")


@app.route("/cookbook")
def cookbook():
    cookbook = list(Cookbook.query.order_by(Cookbook.cookbook_name).all())
    print(cookbook)
    return render_template("cookbook.html", cookbooks=cookbook)


@app.route("/add_cookbook", methods=["GET", "POST"])
def add_cookbook():
    if request.method == "POST":
        cookbook = Cookbook(cookbook_name=request.form.get("cookbook_name"))
        db.session.add(cookbook)
        db.session.commit()
        return redirect(url_for("cookbook"))
    return render_template("add_cookbook.html")


@app.route("/edit_cookbook/<int:cookbook_id>", methods=["GET", "POST"])
def edit_cookbook(cookbook_id):
    cookbook = Cookbook.query.get_or_404(cookbook_id)
    if request.method == "POST":
        cookbook.cookbook_name = request.form.get("cookbook_name")
        db.session.commit()
        return redirect(url_for("cookbook"))
    return render_template("edit_cookbook.html", cookbook=cookbook)


@app.route("/delete_cookbook/<int:cookbook_id>")
def delete_cookbook(cookbook_id):
    cookbook = Cookbook.query.get_or_404(cookbook_id)
    db.session.delete(cookbook)
    db.session.commit()
    return redirect(url_for("cookbook"))

    
# @app.error(404)
# def page_not_found(e):
#    return render_template("404.html"), 404