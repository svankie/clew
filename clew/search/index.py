__author__ = 'svankiE'

import os

from whoosh.fields import Schema, TEXT as text
from whoosh.index import create_in, open_dir
from whoosh.query import *
from whoosh.qparser import QueryParser

schema = Schema(title=text(stored=True), content=text)

if not os.path.exists("index"):
    os.mkdir("index")

index = create_in("index", schema)
idx = open_dir("index")

writer = idx.writer()
writer.add_document(title=u"your big chance at TV!", content=u"welcome to prime time, bitch!1")
writer.commit()

if __name__ == '__main__':
    try:
        searcher = idx.searcher()
        my_query = And([Term("content", u"prime"), Term("content", u"time")])
        #parser = QueryParser("content", idx.schema)
        #query = parser.parse(my_query)

        res = searcher.search(my_query)
        print len(res)
        print res[0]
    finally:
        searcher.close()