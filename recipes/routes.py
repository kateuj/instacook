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


@app.route("/register", methods=["GET", "POST"])
def register():
    # New user registered
    if request.method == "POST":
        # Check if username exists in database
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

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("user_name").lower()
        flash("Registration successful")
        return redirect(url_for("dashboard", user_name=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in database
        existing_user = Users.query.filter_by(
            user_name=request.form.get("user_name").lower()
        ).first()

        if existing_user:
            # Check password matches the user's input
            if check_password_hash(existing_user.password,
                                   request.form.get("password")):
                session["user"] = request.form.get("user_name").lower()
                flash("Welcome, {}".format(
                        request.form.get("user_name")))
                return redirect(url_for(
                        "dashboard", user_name=session["user"]))
            else:
                # Invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # Remove users from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # Grab the session user's username from db
    user = Users.query.filter_by(user_name=session["user"]).first()
    if user:
        user_id = user.id
        user_cookbook = list(Cookbook.query.filter(
            Cookbook.user_id == user_id).all())
        return render_template("user_dashboard.html", cookbooks=user_cookbook,
                               user_name=user.user_name)

    else:
        # If user is not logged in
        flash("You are not logged in")
        return redirect(url_for("login"))

    return render_template("user_dashboard.html", user_name=user_name)


@app.route("/recipes/<int:id>", methods=["GET"])
# Gets only recipes linked to cookbook_id
def recipes(id):
    cookbook_name = Cookbook.query.get_or_404(id)
    recipes = list(Recipe.query.filter(Recipe.cookbook_id == id).all())
    return render_template("recipes.html", recipes=recipes,
                           cookbook_name=cookbook_name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/search")
def search():

    # Get the query parameters from the requests below
    dish_origin = request.args.get('dish_origin')
    star_rating = request.args.get('star_rating')
    meal_type = request.args.get('meal_type')
    recipes = Recipe.query.filter(Recipe.dish_origin == dish_origin if
                                  dish_origin else True,
                                  Recipe.star_rating == star_rating if
                                  star_rating else True,
                                  Recipe.meal_type == meal_type if
                                  meal_type else True
                                  ).all()
    # Distinct query ensure no duplicates are displayed
    distinct_dish_origins = Recipe.query.distinct('dish_origin').all()
    # Selected keeps user's choice visible when URL link updates
    return render_template("search.html", recipes=recipes,
                           selected_meal_type=meal_type,
                           selected_star_rating=star_rating,
                           dish_origins=[i.dish_origin for i in
                                         distinct_dish_origins],
                           selected_dish_origin=dish_origin)


@app.route("/add_cookbook", methods=["GET", "POST"])
# Posts new cookbook name linked to username
def add_cookbook():
    if request.method == "POST":
        cookbook = Cookbook(cookbook_name=request.form.get("cookbook_name"))
        user = Users.query.filter_by(user_name=session["user"]).first()
        cookbook.user_id = user.id
        db.session.add(cookbook)
        db.session.commit()
        flash("Cookbook created")
        return redirect(url_for("dashboard"))
    return render_template("add_cookbook.html")


@app.route("/edit_cookbook/<int:cookbook_id>", methods=["GET", "POST"])
# Use cookbook ID to locate and edit specific cookbook name
def edit_cookbook(cookbook_id):
    cookbook = Cookbook.query.get_or_404(cookbook_id)
    if request.method == "POST":
        cookbook.cookbook_name = request.form.get("cookbook_name")
        db.session.commit()
        flash("Cookbook updated")
        return redirect(url_for("dashboard"))
    return render_template("edit_cookbook.html", cookbook=cookbook)


@app.route("/delete_cookbook/<int:cookbook_id>")
# Use cookbook ID to locate and delete cookbook and all recipes linked to it
def delete_cookbook(cookbook_id):
    cookbook = Cookbook.query.get_or_404(cookbook_id)
    db.session.delete(cookbook)
    db.session.commit()
    return redirect(url_for("dashboard"))


@app.route("/add_recipe", methods=["GET", "POST"])
# Add recipe linked to chosen cookbook name
def add_recipe():
    user = Users.query.filter_by(user_name=session["user"]).first()
    if user:
        user_id = user.id
        user_cookbook = list(Cookbook.query.filter(
            Cookbook.user_id == user_id).all())
    cookbook = list(Cookbook.query.order_by(Cookbook.cookbook_name).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_instructions=request.form.get("recipe_instructions"),
            dish_origin=request.form.get("dish_origin"),
            meal_type=request.form.get("meal_type"),
            star_rating=request.form.get("star_rating"),
            cookbook_id=request.form.get("cookbook_id")
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe added")
        return redirect(url_for("dashboard"))
    return render_template("add_recipe.html", cookbooks=user_cookbook)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
# Edit specific recipe using recipe_id
def edit_recipe(recipe_id):
    user = Users.query.filter_by(user_name=session["user"]).first()
    if user:
        user_id = user.id
        user_cookbook = list(Cookbook.query.filter(
            Cookbook.user_id == user_id).all())
    recipe = Recipe.query.get_or_404(recipe_id)
    cookbook = list(Cookbook.query.order_by(Cookbook.cookbook_name).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name"),
        recipe.recipe_ingredients = request.form.get("recipe_ingredients"),
        recipe.recipe_instructions = request.form.get("recipe_instructions"),
        recipe.dish_origin = request.form.get("dish_origin"),
        recipe.star_rating = request.form.get("star_rating"),
        recipe.meal_type = request.form.get("meal_type"),
        recipe.cookbook_id = request.form.get("cookbook_id")
        db.session.commit()
        flash("Recipe updated")
        return redirect(url_for("dashboard"))
    return render_template("edit_recipe.html", recipe=recipe,
                           cookbooks=user_cookbook)


@app.route("/delete_recipe/<int:recipe_id>")
# Delete specific recipe using recipe_id
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted from cookbook")
    return redirect(url_for("dashboard"))


@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 