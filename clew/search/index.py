__author__ = 'svankiE'

from whoosh.fields import Schema, TEXT, ID

schema = Schema(
    title=TEXT(stored=True),
    description=TEXT(stored=True),
    date=ID)