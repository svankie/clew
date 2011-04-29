__author__ = 'svankiE'

from clew.db import db

class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column("event_name", db.String(256))
    date = db.Column("event_date", db.DateTime)
    description = db.Column("event_description", db.String(2048))

    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description