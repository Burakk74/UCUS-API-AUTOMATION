import pytest
from utils.api_client import FlightAPIClient



@pytest.fixture(scope="session")
def api_client():
    """Fixture to provide an instance of the FlightAPIClient."""
    client = FlightAPIClient()
    return client



