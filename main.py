from scraper.scraper import PageScraper
from scraper.parser import OutletParser
from scraper.service import McDonaldsLocatorService

if __name__ == "__main__":
    scraper = PageScraper("Kuala Lumpur")
    parser = OutletParser()
    service = McDonaldsLocatorService(scraper, parser)

    results = service.get_outlets()

    for i, r in enumerate(results, 1):
        print(f"\nOutlet {i}")
        for k, v in r.items():
            print(f"{k.capitalize():<12}: {', '.join(v) if isinstance(v, list) else v}")
