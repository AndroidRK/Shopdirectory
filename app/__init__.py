
from flask import Flask
from app.MainBlueprints import main


def create_app():
    app = Flask(__name__,template_folder='templates')
    app.register_blueprint(main)
    return app