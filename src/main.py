from flask import Flask

from database.db import db, SQLALCHEMY_DATABASE_URI


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
