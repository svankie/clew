from clew.scraping.parsers import GenericRSSParser

__author__ = 'svankiE'

# obviously, this is going to be increasingly CRAZY, when new scrapers arrive.

if __name__ == '__main__':
    feeds = [
        # so?
    ]
    scraper = GenericRSSParser(feeds)
    scraper.retrieve_events()