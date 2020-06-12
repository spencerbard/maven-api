""" Test setup for maven assessment api """
import os
import tempfile

import pytest

from api import create_app, DB


@pytest.fixture()
def app():
    """ Fixture for app initialized with test config. """
    db_fd, db_path = tempfile.mkstemp()

    app = create_app(
        {
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )
    with app.app_context():
        DB.create_all()
    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture()
def client(app):
    """ Fixture for test client """
    return app.test_client()
