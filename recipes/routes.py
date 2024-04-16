from flask import render_template, request, redirect, url_for, session, flash
from recipes import app, db
from recipes.models import Users, Cookbook, Recipe
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    recipes = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user and log them in."""
    if request.method == "POST":
        # Check if username already exists in DB
        existing_user = Users.query.filter_by(
            user_name=request.form.get("user_name")
        ).first()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Register new user
        new_user = Users(
            user_name=request.form.get("user_name").lower(),
            password=generate_password_hash(request.form.get("password")),
        )
        db.session.add(new_user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("user_name").lower()
        flash("Registration successful")
        return redirect(url_for("dashboard", user_name=session["user"]))

    return render_template("register.html")

    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter_by(
            user_name=request.form.get("user_name").lower()
        ).first()

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user.password, request.form.get("password")):
                    session["user"] = request.form.get("user_name").lower()
                    flash("Welcome, {}".format(
                        request.form.get("user_name")))
                    return redirect(url_for(
                        "dashboard", user_name=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove users from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/dashboard/<user_name>", methods=["GET", "POST"])
def dashboard(user_name):
    # grab the session user's username from db
    user = Users.query.filter_by(user_name=session["user"]).first()
    if user:
        user_name = user.user_name

        # add else statement for no user in session
    return render_template("user_dashboard.html", user_name=user_name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/search")
def search():
    return render_template("search.html")


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


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    cookbook = list(Cookbook.query.order_by(Cookbook.cookbook_name).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_instructions=request.form.get("recipe_instructions"),
            dish_origin=request.form.get("dish_origin"),
            star_rating=request.form.get("star_rating"),
            cookbook_id=request.form.get("cookbook_id")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("cookbook"))
    return render_template("add_recipe.html", cookbook=cookbook)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    cookbook = list(Cookbook.query.order_by(Cookbook.cookbook_name).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name"),
        recipe.recipe_ingredients = request.form.get("recipe_ingredients"),
        recipe.recipe_instructions = request.form.get("recipe_instructions"),
        recipe.dish_origin = request.form.get("dish_origin"),
        recipe.star_rating = request.form.get("star_rating"),
        recipe.cookbook_id = request.form.get("cookbook_id")
        db.session.commit()
    return render_template("edit_recipe.html", recipe=recipe, cookbook=cookbook)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("recipes"))


# @app.error(404)
# def page_not_found(e):
#    return render_template("404.html"), 404