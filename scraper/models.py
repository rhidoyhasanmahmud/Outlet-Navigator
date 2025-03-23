from typing import List

class Outlet:
    def __init__(self, name: str, address: str, phone: str, latitude: float, longitude: float, features: List[str], waze_link: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.latitude = latitude
        self.longitude = longitude
        self.features = features
        self.waze_link = waze_link

    def to_dict(self):
        return self.__dict__
