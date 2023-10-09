"""Flask app for Cupcakes"""
import os

from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake, DEFAULT_IMAGE_URL

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
    """Get all cupcake data returns JSON like {cupcakes: [{id, flavor, size, rating, image_url}, ...]}"""

    cupcakes = Cupcake.query.all()
    cupcakes_serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=cupcakes_serialized)


@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Get data about a single cupcake, returns JSON like {cupcake: {id, flavor, size, rating, image_url}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()

    return jsonify(cupcake=serialized_cupcake)


@app.post("/api/cupcakes")
def create_cupcake():
    """Take flavor, size, rating and image data and create new cupcake,
    returns JSON like {cupcake: {id, flavor, size, rating, image_url}}"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"] or None

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image_url=image_url,
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = new_cupcake.serialize()

    return (jsonify(cupcake=serialized_cupcake), 201)


@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Update a cupcake using the id passed in the URL and the
    cupcake data passed in the body of the request . Return JSON like
     {cupcake: {id, flavor, size, rating, image_url}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake_modification = request.json
    for key in cupcake_modification:
        if not cupcake_modification[key]:
            cupcake_modification[key] = None

    cupcake.flavor = (
        cupcake_modification.get("flavor")
        if cupcake_modification.get("flavor")
        else cupcake.flavor
    )

    cupcake.size = (
        cupcake_modification.get("size")
        if cupcake_modification.get("size")
        else cupcake.size
    )

    cupcake.rating = (
        cupcake_modification.get("rating")
        if cupcake_modification.get("rating")
        else cupcake.rating
    )

    cupcake.image_url = (
        cupcake_modification.get("image_url")
        if cupcake_modification.get("image_url")
        else cupcake.image_url
    )

    db.session.commit()

    serialized_cupcake = cupcake.serialize()
    return jsonify(cupcake=serialized_cupcake)

@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Deletes the specified cupcake, returns JSON like
    {deleted: [cupcake-id]}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted=[cupcake_id])

