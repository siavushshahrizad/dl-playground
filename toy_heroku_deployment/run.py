"""
Name: run.py
Created: 9.12.24
---------------
Entry point for the Flask application. Initializes and runs 
the app on host 0.0.0.0 and the port specified by the PORT 
environment variable or defaults to 5000.
"""

import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)