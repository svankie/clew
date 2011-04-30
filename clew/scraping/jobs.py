from clew.scraping.parsers import GenericRSSParser

__author__ = 'svankiE'

# obviously, this is going to be increasingly CRAZY, when new scrapers arrive.

if __name__ == '__main__':
    feeds = [
        "http://ws.audioscrobbler.com/1.0/artist/Pain%2Bof%2BSalvation/events.rss",
        "http://ws.audioscrobbler.com/1.0/artist/Imogen%2BHeap/events.rss"
    ]
    scraper = GenericRSSParser(feeds)
    scraper.retrieve_events()