__author__ = 'svankiE'

from whoosh.fields import SchemaClass, TEXT, DATETIME, NUMERIC
from whoosh.analysis import StemmingAnalyzer

class EventSchema(SchemaClass):

    id = NUMERIC(stored=True, unique=True)
    title = TEXT(stored=True, analyzer=StemmingAnalyzer(), field_boost=1.5)
    description = TEXT(stored=True, analyzer=StemmingAnalyzer(), field_boost=1.0)
    date = DATETIME(stored=True)