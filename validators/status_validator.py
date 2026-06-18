def validate_status(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected {expected_status}, got {response.status_code}"
    )