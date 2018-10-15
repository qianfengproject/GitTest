from flask import Flask
from flask_session import Session

from APP.apis import init_blue
from APP.ext import init_ext


def create_app():
    app = Flask(__name__)
    init_blue(app=app)
    init_ext(app=app)
    return app