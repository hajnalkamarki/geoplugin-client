# location class
class Location:

    # constructor gives values to all the parameters of the class
    def __init__(self, city: str, region: str, country: str, latitude: float, longitude: float, timezone: str):
        self.city = city
        self.region = region
        self.country = country
        self.latitude = latitude,
        self.longitude = longitude,
        self.timezone = timezone
