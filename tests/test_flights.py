import pytest
from utils.models import FlightResponse

# Test Data: List of regions with their bounding box coordinates
regions = [
    ("Turkey", 36.0, 26.0, 42.0, 45.0),
    ("UK", 49.0, -8.6, 59.4, 1.7),
    ("Germany", 47.2, 5.8, 55.0, 15.0),
]

def test_get_all_flights_successfully(api_client):
    """
    Positive Test: Fetch all active flights and verify response structure.
    Expected: Status Code 200 and 'states' key should be a list.
    """
    response = api_client.get_flights()
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    
    data = response.json()
    assert "states" in data, "Response body should contain 'states' key"
    assert isinstance(data["states"], list), "'states' should be a list"

def test_flight_data_integrity(api_client):
    """
    Data Integrity Test: Verify that the first flight in the list has a valid ID.
    """
    response = api_client.get_flights()
    data = response.json()
    states = data.get("states")
    
    if states and len(states) > 0:
        first_flight_id = states[0][0]
        print(f"\n[INFO] First flight unique ID (icao24): {first_flight_id}")
        assert first_flight_id is not None, "Flight ID should not be null"
    else:
        pytest.skip("No flight data available at the moment.")

def test_get_flights_with_invalid_endpoint(api_client):
    """
    Negative Test: Accessing a non-existent endpoint should return 404.
    """
    response = api_client.get_invalid_endpoint()
    assert response.status_code == 404, f"Expected 404, but got {response.status_code}"
    print(f"\n[INFO] Server error message: {response.text}")

@pytest.mark.parametrize("region_name, lamin, lomin, lamax, lomax", regions)
def test_get_flights_by_region_and_validate_schema(api_client, region_name, lamin, lomin, lamax, lomax):
    """
    Data-Driven Test: Fetch flights by coordinates and validate the JSON schema using Pydantic.
    """
    # 1. API Request
    response = api_client.get_flights_by_coords(lamin, lomin, lamax, lomax)
    
    # 2. Status Code Assertion
    assert response.status_code == 200, f"Request failed for {region_name} with status {response.status_code}"

    # 3. Pydantic Schema Validation
    try:
        # Validates the entire JSON structure against the FlightResponse model
        FlightResponse(**response.json())
        print(f"\n[SUCCESS] Schema validation passed for {region_name}.")
    except Exception as e:
        pytest.fail(f"Schema validation failed for {region_name}: {e}")

    # 4. Log the count for verification
    data = response.json()
    flight_count = len(data["states"]) if data["states"] is not None else 0
    print(f"[INFO] Active flights in {region_name}: {flight_count}")