__author__ = 'svankiE'

from clew.core.model import Event
from clew.search.index_builder import IndexBuilder

if __name__ == '__main__':
    print "Building object index..."
    builder = IndexBuilder()
    events = Event.query.all()

    if events:
        # for now, building clean, shiny indexes.
        builder.build_index(events, clean=True)
        print "Done."
    else:
        print "No events to be added."