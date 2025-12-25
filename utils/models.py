from pydantic import BaseModel, field_validator
from typing import List, Optional

class FlightState(BaseModel):
    # The structure of each flight within the list returned from the API.
    #
    # OpenSky returns each flight as a list; let's just verify the first few.
    icao24: str
    callsign: Optional[str]
    origin_country: str

class FlightResponse(BaseModel):
    time: int
    states: Optional[List[list]] # Flights are returned as a list of lists