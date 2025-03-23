from scraper.scraper import PageScraper
from scraper.parser import OutletParser

class McDonaldsLocatorService:
    def __init__(self, scraper: PageScraper, parser: OutletParser):
        self.scraper = scraper
        self.parser = parser

    def get_outlets(self):
        html = self.scraper.load_page()
        outlets = self.parser.parse(html)
        return [outlet.to_dict() for outlet in outlets]
