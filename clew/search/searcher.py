__author__ = 'svankiE'

from whoosh.index import open_dir
from whoosh.qparser.default import QueryParser

class EventSearcher(object):

    def __init__(self):
        index = open_dir("search/index")
        self.searcher = index.searcher()
        self.parser = QueryParser("description", index.schema)

    def search(self, query):

        data = None
        try:
            query = self.parser.parse(query)
            result = self.searcher.search(query)
            data = [{"title": res["title"], "description": res["description"], "id": res["id"]} for res in result]
        finally:
            self.searcher.close()

        return data