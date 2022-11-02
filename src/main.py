from config import FlaskConfig
from flask import Flask
from library.exceptions import BaseException, exception_handler
from swagger import initialize_flasgger


def create_app():
    try:
        app = Flask(__name__)

        initialize_flasgger(app)
        app.register_error_handler(BaseException, exception_handler)

        config = FlaskConfig()
        app.config.from_object(config)

        return app
    except Exception as e:
        raise Exception(f"Error while creating app: {e}")


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
