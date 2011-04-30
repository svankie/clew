__author__ = 'svankiE'

import os

from whoosh.index import create_in
from clew.search.index import schema

class IndexBuilder(object):
    """
        Hoping this would be easy enough.
    """
    def __init__(self):
        if not os.path.exists("index"):
            os.mkdir("index")

        index = create_in("index", schema)
        self.writer = index.writer()

    def build(self, events):
        for event in events:
            date = unicode(event.date.strftime('%Y-%m-%d'))
            self.writer.add_document(title=event.name, description=event.description, date=date)
        self.writer.commit()
