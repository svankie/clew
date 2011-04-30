__author__ = 'svankiE'

import os

from whoosh.fields import Schema, TEXT as text, ID as id
from whoosh.index import create_in

schema = Schema(
    title=text(stored=True),
    description=text(stored=True),
    date=id)

if not os.path.exists("index"):
    os.mkdir("index")

index = create_in("index", schema)