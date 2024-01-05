from flask import jsonify, request
from application import app  # app from __init__.py

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Countries API",
        "endpoints": [
            "GET / 200|500",
            "GET /countries"
            "GET /countries/<int:int>",
            "POST /countries",
            "PATCH /countries<int:int>",
            "DELETE /countries<int:int>"
        ]
    }), 200