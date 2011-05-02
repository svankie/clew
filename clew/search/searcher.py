__author__ = 'svankiE'

from datetime import datetime

from whoosh.index import open_dir
from whoosh.qparser.dateparse import DateParserPlugin
from whoosh.qparser.default import MultifieldParser

class EventSearcher(object):

    def search(self, query):
        data = None
        try:
            q = self.parser.parse(query)
            result = self.searcher.search(q)
            data = [
                {"title": res["title"],
                 "description": res["description"],
                 "id": res["id"]
                } for res in result
            ]
        finally:
            # better to close on __del__?
            self.searcher.close()

        return data

    def __init__(self):
        index = open_dir("search/index")
        self.searcher = index.searcher()
        self.parser = MultifieldParser(["title", "description", "date"], index.schema)
        self.parser.add_plugin(DateParserPlugin(free=True))