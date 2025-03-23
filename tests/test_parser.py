from scraper.parser import OutletParser
from scraper.scraper import PageScraper


def test_parse_html():
    scraper = PageScraper()
    html = scraper.load_page()
    parser = OutletParser()
    outlets = parser.parse(html)
    assert isinstance(outlets, list)
    assert len(outlets) > 0
    assert outlets[0].name