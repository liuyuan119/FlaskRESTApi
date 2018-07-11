from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import envs


def create_app():
    app = Flask(__name__)
    app.config.from_object(envs.get('develop'))
    init_ext(app=app)
    init_api(app=app)
    return app
