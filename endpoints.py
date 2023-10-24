from flask import request, jsonify

from app import app
from schemas import *


@app.route("/returnAllIngredients", methods=["GET"])
def returnAllIngredients():
    ingredients_query = ingredients.query.all()
    ingredients_data = [
        {
            "category": i.category,
            "item": i.item,
            "quantity": i.quantity,
            "storageType": i.storageType,
        }
        for i in ingredients_query
    ]
    return jsonify(ingredients_data)


@app.route("/returnAllRecipes", methods=["GET"])
def returnAllRecipes():
    # Query all recipes
    recipes_query = recipes.query.all()
    recipes_data = []

    # Iterate through each recipe to gather its details, ingredients, and directions
    for recipe in recipes_query:
        recipe_dict = {
            "id": recipe.id,
            "name": recipe.name,
            "description": recipe.description,
            "ingredients": [],
            "directions": []
        }

        # Query ingredients for this recipe
        ingredients_query = recipeingredients.query.filter_by(recipe_id=recipe.id).all()
        for ingredient in ingredients_query:
            recipe_dict["ingredients"].append(ingredient.ingredient)

        # Query directions for this recipe
        directions_query = recipedirections.query.filter_by(recipe_id=recipe.id).all()
        for direction in directions_query:
            recipe_dict["directions"].append(direction.direction)

        # Append this recipe's data to the list
        recipes_data.append(recipe_dict)

    # Convert the list to JSON and return
    return jsonify(recipes_data)

@app.route("/updatePantry", methods=["POST"])
def updatePantry():
    from app import db
    data = request.json  # Assumes the client sends JSON data

    # Validate the data before saving
    if not all(key in data for key in ("category", "item", "quantity", "storageType")):
        return jsonify({"error": "Missing data"}), 400

    # Create a new Ingredient object
    new_ingredient = ingredients(
        category=data["category"],
        item=data["item"],
        quantity=data["quantity"],
        storageType=data["storageType"],
    )

    # Add the new ingredient to the database
    db.session.add(new_ingredient)
    db.session.commit()

    return jsonify({"message": "Ingredient saved successfully!"}), 201


@app.route("/send_message", methods=["POST"])
def send_message():
    from app import messages
    from functions import send_message

    data = request.json
    message_content = data.get("message_content")
    messages.append({"role": "user", "content": message_content})
    replied_message = send_message(messages)
    messages.append({"role": "assistant", "content": replied_message})
    return jsonify({"status": "success", "message": replied_message})
