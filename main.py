from scraper.scraper import PageScraper
from scraper.parser import OutletParser
from scraper.service import McDonaldsLocatorService
from scraper.models import OutletDB
from database.db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

def store_to_db(outlets):
    db = SessionLocal()
    for o in outlets:
        record = OutletDB(
            name=o['name'],
            address=o['address'],
            phone=o['phone'],
            latitude=o['latitude'],
            longitude=o['longitude'],
            features=", ".join(o['features']),
            waze_link=o['waze_link']
        )
        db.add(record)
    db.commit()
    print("Saved to DB:", db.query(OutletDB).count())

    db.close()

if __name__ == "__main__":
    scraper = PageScraper()
    parser = OutletParser()
    service = McDonaldsLocatorService(scraper, parser)
    outlets = service.get_outlets()
    store_to_db(outlets)
    print(f"Stored {len(outlets)} outlets in the database.")
