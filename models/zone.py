from .basemodel import BaseModel
from .types.location import Location
from typing import List


class Zone(BaseModel):
    name: str
    description: str
    locations: List[Location]

    def __init__(self, name: str = None, description: str = None, locations: List[Location] = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        if locations is not None:
            _locations = []
            for location in locations:
                if isinstance(location, dict):
                    _locations.append(Location(**location))
                else:
                    _locations.append(location)
            self.locations = _locations
        else:
            self.locations = locations
