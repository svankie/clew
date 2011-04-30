__author__ = 'svankiE'

from clew.db import db

events_artists = db.Table('events_artists',
    db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
    db.Column("artist_id", db.Integer, db.ForeignKey("artists.id"))
)

events_venues = db.Table('events_venues',
    db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
    db.Column("venue_id", db.Integer, db.ForeignKey("venues.id"))
)

events_users = db.Table('events_users',
    db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
)

agendas_events = db.Table('agendas_events',
    db.Column("agenda_id", db.Integer, db.ForeignKey("agendas.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("events.id"))
)

class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column("event_name", db.String(256))
    date = db.Column("event_date", db.DateTime)
    description = db.Column("event_description", db.String(2048))

    artists = db.relation('Artist', secondary=events_artists, backref=db.backref('events'))
    venues = db.relation('Venue', secondary=events_venues, backref=db.backref('events'))
    users = db.relation('User', secondary=events_users, backref=db.backref('events'))

    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column("artist_name", db.String(64))
    description = db.Column("artist_description", db.String(2048))

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column("venue_name", db.String(64))
    description = db.Column("venue_description", db.String(2048))

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Agenda(db.Model):
    __tablename__ = 'agendas'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User")
    events = db.relationship("Event", secondary=agendas_events, backref=db.backref('agendas'))

    def __init__(self, user):
        self.user = user

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    full_name = db.Column(db.String(64))
    username = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(8))

    def __init__(self, full_name, username, email, password):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password

class Shout(db.Model):
    __tablename__ = 'shouts'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    message = db.Column(db.Text)

    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message
        
class Invitation(db.Model):
    __tablename__ = 'invitations'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rsvp = db.Column(db.Boolean, default=False)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, rsvp, event_id, user_id):
        self.rsvp = rsvp
        self.event_id = event_id
        self.user_id = user_id

class Wishlist(db.Model):
    __tableame__ = 'wishlists'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, user_id):
        self.user_id = user_id

class LoopingSearch(db.Model):
    __tablename__ = 'looping_searches'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    wishlist_id = db.Column(db.Integer, db.ForeignKey("wishlists.id"))
    query = db.Column(db.Text)

    def __init__(self, user_id, wishlist_id, query):
        self.user_id = user_id
        self.wishlist_id = wishlist_id
        self.query = query

        