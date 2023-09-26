
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for mockup purposes
ingredients_data = [
    {
        "category": "Vegetables",
        "item": "Broccoli",
        "quantity": 1,
        "storageType": "unit"
    }
    # ... other ingredients
]

recipes_data = [
    {
        "name": "Spaghetti Carbonara",
        "description": "A classic Italian dish.",
        "ingredients": ["Spaghetti", "Eggs", "Pancetta", "Parmesan cheese"],
        "directions": ["Cook spaghetti.", "Mix eggs and cheese.", "Fry pancetta.", "Combine all ingredients."]
    }
    # ... other recipes
]


@app.route("/returnAllIngredients", methods=["GET"])
def returnAllIngredients():
    # For now, returning the sample data. In a real setup, you'd query the database.
    return jsonify(ingredients_data)


@app.route("/returnAllRecipes", methods=["GET"])
def returnAllRecipes():
    # For now, returning the sample data. In a real setup, you'd query the database.
    return jsonify(recipes_data)


@app.route("/updatePantry", methods=["POST"])
def updatePantry():
    data = request.json
    # In a real setup, you'd update the database with the received data.
    return jsonify({"status": "success", "message": "Pantry updated successfully!"})


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    message_content = data.get("message_content")
    # For now, just echoing the message. In a real setup, you'd process the message using GPT.
    return jsonify({"status": "success", "message": message_content})


if __name__ == "__main__":
    app.run(port=4000, debug=True)
