__author__ = 'svankiE'

import os

from whoosh.index import create_in

from clew.search.schemas import EventSchema
from clew.core.model import Event

class IndexBuilder(object):
    """
        Hoping this would be easy enough.
    """
    def __init__(self):
        if not os.path.exists("index"):
            os.mkdir("index")

        index = create_in("index", EventSchema())
        self.searcher = index.searcher()
        self.writer = index.writer()

    ##########
    ## I need to store a last-modified date to implement a silly
    ## way to build my index from scrath (if I want) or to build
    ## it incrementally (that I totally want now). TODO.
    ####

    def build_index(self, events, clean=False):
        if clean:
            self.scratch_build(events)
        else:
            self.incremental_build(events)

    def incremental_build(self, events):
        indexed_events = set()
        events_to_index = set()

        searcher = self.searcher
        writer = self.writer

        for fields in searcher.all_stored_fields():
            indexed_event = fields['id']
            indexed_events.add(indexed_event)

            if Event.query.get_by_id(indexed_event) is None:
                # it has been deleted
                writer.delete_by_term('id', indexed_event)
            else:
                # check for modifications
                indexed_time = fields['time']
                mtime = fields['last_modified_time']
                if mtime > indexed_time:
                    # it has been modified
                    writer.delete_by_term('id', indexed_event)
                    events_to_index.add(indexed_event)

        for event.id in events_to_index or event.id not in indexed_events:
            writer.add_document(self.get_values(event))
        writer.commit(optimize=True)

    def scratch_build(self, events):
        writer = self.writer
        for event in events:
            writer.add_document(**self.get_values(event))
        writer.commit(merge=False)

    def get_values(self, event):
        return dict([(k,v) for k,v in event.to_json(from_builder=True).items() if v is not None])