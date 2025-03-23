from bs4 import BeautifulSoup
from scraper.models import Outlet
import json

class OutletParser:
    def parse(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        outlet_blocks = soup.select(".addressBox")
        outlets = []

        for block in outlet_blocks:
            script_tag = block.find("script", type="application/ld+json")
            if not script_tag:
                continue

            try:
                data = json.loads(script_tag.string)
                name = data.get("name")
                address = data.get("address")
                phone = data.get("telephone")
                lat = data.get("geo", {}).get("latitude")
                lng = data.get("geo", {}).get("longitude")
            except:
                continue

            features = [
                tooltip.get_text(strip=True)
                for tooltip in block.select(".ed-tooltiptext")
                if tooltip.get_text(strip=True)
            ]

            waze_link = ""
            for a in block.find_all("a"):
                if a.text.strip().lower() == "waze":
                    waze_link = a.get("href", "")
                    break

            outlet = Outlet(name, address, phone, lat, lng, features, waze_link)
            outlets.append(outlet)

        return outlets
