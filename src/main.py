import os

from flask import Flask
from swagger import initialize_flasgger

app = Flask(__name__)

swagger = initialize_flasgger(app)


if __name__ == "__main__":
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(host="0.0.0.0", debug=DEBUG)
