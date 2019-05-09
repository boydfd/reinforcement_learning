from .location import Location


class LocationFactory:
    def __init__(self):
        self.first = [Location(i, 3, 3) for i in range(21)]
        self.second = [Location(i, 4, 2) for i in range(21)]


location_factory = LocationFactory()
