from recipes import db

class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    cookbook = db.relationship('Cookbook', backref='user', cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.username

class Cookbook(db.Model):
    # schema for the Cookbook model
    id = db.Column(db.Integer, primary_key=True)
    cookbook_name = db.Column(db.String(25), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="cookbook", cascade="all, delete", lazy=True)
    user_id = db.relationship(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.coobook_name

class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_instructions = db.Column(db.Text, nullable=False)
    dish_origin = db.Column(db.String(50), nullable=False)
    star_rating = db.Column(db.Integer, nullable=False)
    cookbook_id = db.relationship(db.Integer, db.ForeignKey("cookbook.id", ondelete="CASCADE"))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Recipe Name: {1} | Star Rating: {2} | Ingredients: {3} | Instructions: {4}".format(
            self.id, self.recipe_name, self.star_rating, self.recipe_ingredients, self.recipe_instructions
        )

# potential class for recipe ingredients and instructions