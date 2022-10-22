from config import FlaskConfig
from flask import Flask
from swagger import initialize_flasgger

app = Flask(__name__)

swagger = initialize_flasgger(app)


if __name__ == "__main__":
    config = FlaskConfig()
    app.config.from_object(config)
    app.run(host="0.0.0.0", port=5000)
