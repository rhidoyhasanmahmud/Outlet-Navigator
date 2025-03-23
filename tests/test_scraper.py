from scraper.scraper import PageScraper

def test_load_page():
    scraper = PageScraper()
    html = scraper.load_page()
    assert isinstance(html, str)
    assert "html" in html.lower()