"""Flask app for Cupcakes"""
import os

from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

# app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
# debug = DebugToolbarExtension(app)


@app.get("/api/cupcakes")
def get_all_cupcake_data():
    """Get all cupcake data returns JSON"""

    cupcakes = Cupcake.query.all()
    cupcakes_serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=cupcakes_serialized)


@app.get("/api/cupcakes/<cupcake_id>")
def get_cupcake(cupcake_id):
    """Get data about a single cupcake, returns JSON"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()

    return jsonify(cupcake=serialized_cupcake)


@app.post("/api/cupcakes")
def create_cupcake():
    """Creates a new cupcake, returns JSON"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"]

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = new_cupcake.serialize()

    return (jsonify(cupcake=serialized_cupcake), 201)
