import os

from flask import Flask
from swagger import initialize_flasgger

app = Flask(__name__)

swagger = initialize_flasgger(app)


if __name__ == "__main__":
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY").encode()

    if not SECRET_KEY:
        raise Exception("FLASK_SECRET_KEY not set")

    app.secret_key = SECRET_KEY
    app.run(host="0.0.0.0", debug=DEBUG)
