""" Models for maven assessment db. """
from api import DB


class NumberCount(DB.Model):
    """ Model for storing number counts. """

    __tablename__ = "number_count"
    number = DB.Column(DB.Integer, primary_key=True)
    count = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        """ Return str representation of NumberCount obj. """
        return f"<NumberCount {self.number}: {self.count}>"
