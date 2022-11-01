from flask import Flask, jsonify
from library.exceptions import BaseException


def initialize_error_handlers(app: Flask):
    app.register_error_handler(BaseException, exception_handler)
    app.register_error_handler(400, handle_400)
    app.register_error_handler(401, handle_401)
    app.register_error_handler(403, handle_403)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(405, handle_405)
    app.register_error_handler(409, handle_409)
    app.register_error_handler(412, handle_412)
    app.register_error_handler(500, handle_500)


def exception_handler(e):
    return jsonify(error=str(e)), e.status_code


def handle_400(e):
    return jsonify(error=str(e.description)), 400


def handle_401(e):
    return jsonify(error=str(e.description)), 401


def handle_403(e):
    return jsonify(error=str(e.description)), 403


def handle_404(e):
    return jsonify(error=str(e.description)), 404


def handle_405(e):
    return jsonify(error=str(e.description)), 405


def handle_409(e):
    return jsonify(error=str(e.description)), 409


def handle_412(e):
    return jsonify(error=str(e.description)), 412


def handle_500(e):
    return jsonify(error=str(e.description)), 500
