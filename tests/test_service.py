from scraper.service import McDonaldsLocatorService
from scraper.scraper import PageScraper
from scraper.parser import OutletParser


def test_service_pipeline():
    service = McDonaldsLocatorService(PageScraper(), OutletParser())
    data = service.get_outlets()
    assert isinstance(data, list)
    assert "name" in data[0]
