""" Default api config. """
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Default api config class. """

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/sqlite.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
