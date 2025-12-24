import pytest



def get_all_flights_successfully(api_client):
    """Positive test case: Fetch all flights successfully.(It should return status code 200)"""

    #Request to API
    response = api_client.get_flights()

    #2 Asserts: Check the responses
    assert response.status_code == 200,f"Expected status code 200, but got {response.status_code}"


    """Is the response data structure correct? (It should contain 'states' as a list)"""
    data = response.json()
    assert "states" in data
    assert isinstance(data["states"], list)


    """Negative test case: Fetch flight details with invalid ID.(It should return status code 404)"""

    invalid_flight_id = "9999999999"

    #Request with invalid flight ID to API
    response = api_client.get_flight_details(invalid_flight_id)

    #Assert: Check the response status code (should be 404)
    assert response.status_code == 404,f"Expected status code 404 for invalid flight ID, but got {response.status_code}"


def test_flight_data_structure(api_client):
    """It checks for the presence of required fields  within the flight data."""
    response = api_client.get_flights()
    data = response.json()
    
    # Check if 'states' key exists and is a list
    assert "states" in data, "'states' key is missing in the response"

    # Check List : Is states is a list and not full
    states = data["states"]
    if states is not None and len(states) > 0:
        first_flight= states[0]
        
        assert first_flight[0] is not None
        print(f"\nFirst flight ID: {first_flight[0]}")    
    else:
        pytest.skip("No flight data available to test.")
    


    def test_get_flights_with_invalid_endpoint(api_client):
        """
        Negative scenario: When an invalid endpoint is requested, a 404 error should be returned.
        """
        # 1. Request to invalid endpoint
        response = api_client.get_invalid_endpoint()
        
        # 2. Assert: Check that the status code is 404
        assert response.status_code == 404, f"Expected 404, but got {response.status_code}!"

        # Optional: Check the error message content (if API supports it)
        print(f"\nError message returned by server: {response.text}")