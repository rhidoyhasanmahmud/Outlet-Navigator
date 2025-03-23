from playwright.sync_api import sync_playwright

class PageScraper:
    def __init__(self, state: str = "Kuala Lumpur"):
        self.state = state

    def load_page(self) -> str:
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
