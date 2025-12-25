import httpx


class FlightAPIClient:
    def __init__(self):
        # Main address for the API)
        self.base_url ="https://opensky-network.org/api"


        #Headers that will be common to all requests (JSON data type)
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }


    def get_flights(self):
        """Fetch a list of flights from the API."""
        url = f"{self.base_url}/states/all"
        response = httpx.get(url, headers=self.headers)
        
        return response
    

    def get_flight_details(self, flight_id):
        """Fetch details of a specific flight by ID."""
        response = httpx.get(
            f"{self.base_url}/flights/{flight_id}",
            headers=self.headers)
        
        return response
    


    def get_invalid_endpoint(self):
        """Request to an invalid endpoint."""
        # 'states/all' we use invalid path here
        response = httpx.get(f"{self.base_url}/wrong/path", headers=self.headers)
        return response


    def get_flights_by_coords(self, lamin, lomin, lamax, lomax):
        """Fetch flights within specified geographic coordinates."""

        params = {
            "lamin": lamin,
            "lomin": lomin,
            "lamax": lamax,
            "lomax": lomax
        }

        response = httpx.get(f"{self.base_url}/states/all", params=params, headers=self.headers)
        return response