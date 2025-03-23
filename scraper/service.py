from scraper.scraper import PageScraper
from scraper.parser import OutletParser

class McDonaldsLocatorService:
    def __init__(self, scraper, parser):
        self.scraper = scraper
        self.parser = parser

    def get_outlets(self):
        html = self.scraper.load_page()
        return [o.to_dict() for o in self.parser.parse(html)]