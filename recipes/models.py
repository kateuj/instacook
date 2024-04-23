from recipes import db


class Users(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    cookbook = db.relationship('Cookbook', backref='users',
                               cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name


class Cookbook(db.Model):
    # schema for the Cookbook model
    id = db.Column(db.Integer, primary_key=True)
    cookbook_name = db.Column(db.String(25), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="cookbook",
                              cascade="all, delete", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey
                        ("users.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.cookbook_name


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_instructions = db.Column(db.Text, nullable=False)
    dish_origin = db.Column(db.String(50), nullable=False)
    meal_type = db.Column(db.String(50), nullable=False)
    star_rating = db.Column(db.Integer, nullable=False)
    cookbook_id = db.Column(db.Integer,
                            db.ForeignKey("cookbook.id", ondelete="CASCADE"))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return (
            f"Recipe ID: {self.id},"
            f"Recipe Name: {self.recipe_name}, "
            f"Star Rating: {self.star_rating}, "
            f"Dish Origin: {self.dish_origin}, "
            f"Meal Type: {self.meal_type}, "
            f"Recipe Ingredients: {self.recipe_ingredients}, "
            f"Recipe Instructions: {self.recipe_instructions}, "
            f"Cookbook ID: {self.cookbook_id}"
            )
