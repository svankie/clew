__author__ = 'svankiE'

import feedparser

from datetime import datetime

from clew.core.model import Event

class GenericRSSParser(object):

    DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'

    def __init__(self, feeds):
        if not feeds:
            raise Exception("You MUST provide at least one feed source.")
        self.feeds = feeds

    def retrieve_events(self):
        """
            reStructuredText
        """
        # te haces el vivo... a ver si este 'caching' funciona.
        feeds = self.feeds
        
        if feeds:
            if not isinstance(feeds, list):
                feeds = list(feeds)
            for feed in feeds:
                r = feedparser.parse(feed)
                for item in r.entries:
                    self.build_event(item)
        else:
            raise Exception("Hey! You just gave me EMPTYNESS.")

        Event.query.session.commit()

    def build_event(self, item):
        title = item.title

        if Event.query.filter_by(name=title).all():
            return -1

        description = item.description
        date = self.get_datetime_obj(item.date)

        ev = Event(title, date, description)
        Event.query.session.add(ev)

    def get_datetime_obj(self, str):
        if str:
            str = str.split("+")[0].strip()
            return datetime.strptime(str, self.DATE_FORMAT)
        else:
            return "bad parsing"


class SongKickParser(object):
    """
        Waiting for the API key.
    """
    def parse(self, feed):
        pass

class FacebookParser(object):
    """
        Waiting for the API key.
    """
    def parse(self, feed):
        pass