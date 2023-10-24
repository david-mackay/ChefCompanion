from flask_sqlalchemy import SQLAlchemy

from app import db


class ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    item = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    storageType = db.Column(db.String(50))


class recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))


class recipeingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    ingredient = db.Column(db.String(50))


class recipedirections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    direction = db.Column(db.String(200))


# Sample data for mockup purposes
ingredients_data = [
    {"category": "Vegetables", "item": "Broccoli", "quantity": 1, "storageType": "unit"}
    # ... other ingredients
]

recipes_data = [
    {
        "name": "Spaghetti Carbonara",
        "description": "A classic Italian dish.",
        "ingredients": ["Spaghetti", "Eggs", "Pancetta", "Parmesan cheese"],
        "directions": [
            "Cook spaghetti.",
            "Mix eggs and cheese.",
            "Fry pancetta.",
            "Combine all ingredients.",
        ],
    }
    # ... other recipes
]
