__author__ = 'svankiE'

from whoosh.fields import Schema, TEXT, DATETIME, NUMERIC

schema = Schema(
    id=NUMERIC(stored=True),
    title=TEXT(stored=True),
    description=TEXT(stored=True),
    date=DATETIME)