__author__ = 'svankiE'

from clew.core.model import Event
from clew.search.index_builder import IndexBuilder

if __name__ == '__main__':
    # TODO: check for duplicates. The Whoosh documentation.

    print "Building object index..."
    idx_builder = IndexBuilder()
    events = Event.query.all()

    if events:
        idx_builder.build(events)
        print "Done."
    else:
        print "No events to be added."