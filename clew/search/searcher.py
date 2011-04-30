__author__ = 'svankiE'

from whoosh.index import open_dir
from whoosh.qparser.default import QueryParser

class EventSearcher(object):

    def __init__(self):
        index = open_dir("search/index")
        self.searcher = index.searcher()
        self.parser = QueryParser("description", index.schema)

    def search(self, query):
        try:
            query = self.parser.parse(query)
            res = self.searcher.search(query)

            return res
        finally:
            self.searcher.close()