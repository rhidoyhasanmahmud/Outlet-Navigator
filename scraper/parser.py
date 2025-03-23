from bs4 import BeautifulSoup
from scraper.models import Outlet
import json

class OutletParser:
    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        blocks = soup.select(".addressBox")
        results = []

        for block in blocks:
            try:
                script = block.find("script", type="application/ld+json")
                data = json.loads(script.string)
                name = data.get("name")
                address = data.get("address")
                phone = data.get("telephone")
                lat = data["geo"]["latitude"]
                lng = data["geo"]["longitude"]
            except:
                continue

            features = [t.get_text(strip=True) for t in block.select(".ed-tooltiptext")]

            waze_link = ""
            for a in block.find_all("a"):
                if a.text.strip().lower() == "waze":
                    waze_link = a.get("href", "")
                    break

            results.append(Outlet(name, address, phone, lat, lng, features, waze_link))
        return results
