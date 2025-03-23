from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./outlets.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# scraper/scraper.py
from playwright.sync_api import sync_playwright

class PageScraper:
    def __init__(self, state="Kuala Lumpur"):
        self.state = state

    def load_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.mcdonalds.com.my/locate-us", timeout=60000)
            page.wait_for_selector("#states")
            page.select_option("#states", label=self.state)
            page.click("#search-now")
            page.wait_for_selector(".addressBox", timeout=15000)
            page.wait_for_timeout(5000)
            html = page.content()
            browser.close()
            return html