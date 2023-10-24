from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://david:Spiritualman!2@localhost:3306/chefcompanion"

CORS(app)  # Enable CORS for all routes
db = SQLAlchemy(app)
messages = []


if __name__ == "__main__":
    with app.app_context():
        from functions import initialize_session

        initialize_session()
        from endpoints import *

    app.run(debug=True, use_reloader=False)
