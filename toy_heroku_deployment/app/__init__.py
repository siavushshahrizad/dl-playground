"""
Name: __init__.py
Created: 9.12.24
---------------
Initializes the Flask application using the factory pattern.
Loads environment variables from .env.production or .env.development
based on the FLASK_ENV setting. Configures application settings
and registers blueprints for route management.
"""

import os
from flask import Flask
from dotenv import load_dotenv
from pathlib import Path

def create_app():
    app = Flask(__name__)

    env_file = Path(__file__).parent.parent / (".env.production" if os.getenv("FLASK_ENV") == "production" else ".env.development")
    
    if env_file.exists():
        load_dotenv(env_file)
    else:
        print(f"Warning: {env_file} not found. Defaults may be used.")

    app.config["DEBUG"] = os.getenv("DEBUG", "False").lower() == "true"

    from .routes import bp
    app.register_blueprint(bp)

    return app