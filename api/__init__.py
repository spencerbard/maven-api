""" App initialization factory for maven assessment api. """
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.config import Config

DB = SQLAlchemy()


# pulled from https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
def create_app(test_config=None):
    """ Create and configure the app.

    Args:
        test_config (dict): optional test config dict to override default configuration
    Returns:
        (Flask instance): Flask app instance
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="MAVEN_ASSESSMENT",
        DATABASE=os.path.join(app.instance_path, "sqlite.db"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    DB.init_app(app)
    from api import models  # noqa
    from api.routes import NUMBER_COUNT

    app.register_blueprint(NUMBER_COUNT)

    return app
