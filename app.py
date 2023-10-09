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


@app.get("/api/cupcakes")
def get_all_cupcake_data():
    """Get all cupcake data returns dictionary"""

    cupcakes = Cupcake.query.all()
    cupcakes_serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=cupcakes_serialized)
