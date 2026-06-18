import pytest

from validators.status_validator import validate_status
from validators.response_validator import validate_json, validate_keys
from validators.schema_validator import validate_schema

from schemas.login_schema import login_schema
from schemas.posts_schema import posts_schema
from schemas.booking_schema import booking_schema


# -------------------------
# MOCK RESPONSE
# -------------------------

class MockResponse:
    def __init__(self, data, status_code=200):
        self._data = data
        self.status_code = status_code

    def json(self):
        return self._data


# -------------------------
# STATUS VALIDATOR TESTS
# -------------------------

def test_validate_status_success():
    response = MockResponse({}, 200)
    validate_status(response, 200)


def test_validate_status_failure():
    response = MockResponse({}, 404)

    with pytest.raises(AssertionError):
        validate_status(response, 200)


# -------------------------
# RESPONSE VALIDATOR TESTS
# -------------------------

def test_validate_json():
    response = MockResponse({"id": 1})
    result = validate_json(response)
    assert result in [None, True]


def test_validate_keys_success():
    response = MockResponse({"id": 1, "name": "Nigam"})
    validate_keys(response, ["id", "name"])


def test_validate_keys_failure():
    response = MockResponse({"id": 1})

    with pytest.raises(AssertionError):
        validate_keys(response, ["id", "name"])


# -------------------------
# SCHEMA VALIDATION TESTS
# -------------------------

def test_login_schema(apis):
    response = apis["reqres"].login()

    assert response.status_code == 200

    validate_schema(response.json(), login_schema)


def test_posts_schema(apis):
    response = apis["jsonplaceholder"].get_posts()

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    validate_schema(data[0], posts_schema)


def test_booking_schema(apis):
    payload = {
        "firstname": "Nigam",
        "lastname": "Shastri",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-06-16",
            "checkout": "2026-06-18"
        }
    }

    response = apis["booking"].create_booking(payload)

    body = response.json()

    assert "booking" in body

    # FIX: validate full response OR correct nested object handling
    validate_schema(body, booking_schema)