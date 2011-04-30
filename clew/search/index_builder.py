from clew.search.index import index
from whoosh.index import open_dir

__author__ = 'svankiE'

class IndexBuilder(object):
    """
        Hoping this would be easy enough.
    """
    def __init__(self):
        ix = open_dir("index")
        self.writer = ix.writer()

    def build(self, events):
        for event in events:
            date = unicode(event.date.strftime('%Y-%m-%d'))
            self.writer.add_document(title=event.name, description=event.description, date=date)
        self.writer.commit()
