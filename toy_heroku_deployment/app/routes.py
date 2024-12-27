"""
Name: routes.py
Created: 9.12.24
---------------
Defines the routes for the Flask application using a blueprint.
Includes endpoints for the home page and agent interaction.
"""

from flask import Blueprint

bp = Blueprint("routes", __name__)

@bp.route("/")
def home():
    return (
        "Welcome to the home page. We are currently building this app, "
        "and you will later be able to interact with it <a href='/agent'>here</a>."
    )

@bp.route("/agent")
def show_agent():
    return (
        "Once we have built the agent, you will be able to interact with it here. "
        "<a href='/'>Return</a> to the home page."
    )