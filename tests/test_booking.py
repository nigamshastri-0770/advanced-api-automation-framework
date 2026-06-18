import pytest
import allure

from utils.data_factory import BookingFactory
from validators.schema_validator import validate_schema
from schemas.booking_schema import booking_schema
from utils.allure_helper import (
    attach_request,
    attach_response,
    attach_execution_time
)


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parallel
@allure.epic("API Automation")
@allure.feature("Booking API")
@allure.story("Create Booking")
@allure.title("Verify user can create booking")
def test_create_booking(apis):

    # ----------------------------
    # Generate test payload
    # ----------------------------
    payload = BookingFactory.create()

    attach_request(payload)

    # ----------------------------
    # API Call
    # ----------------------------
    with allure.step("Create booking"):
        response = apis["booking"].create_booking(payload)

    attach_response(response)
    attach_execution_time(response)

    # ----------------------------
    # Validate status code
    # ----------------------------
    with allure.step("Validate status code"):
        assert response.status_code == 200

    # ----------------------------
    # Parse response
    # ----------------------------
    body = response.json()

    # ----------------------------
    # Validate booking id exists
    # ----------------------------
    with allure.step("Validate booking id"):
        assert "bookingid" in body

    # ----------------------------
    # Validate schema
    # IMPORTANT: pass dict, not response object
    # ----------------------------
    with allure.step("Validate schema"):
        validate_schema(body, booking_schema)

    booking = body["booking"]

    # ----------------------------
    # Validate payload vs response
    # ----------------------------
    with allure.step("Validate booking details"):
        assert booking["firstname"] == payload["firstname"]
        assert booking["lastname"] == payload["lastname"]
        assert booking["totalprice"] == payload["totalprice"]
        assert booking["depositpaid"] == payload["depositpaid"]

    # ----------------------------
    # Response time validation
    # ----------------------------
    with allure.step("Validate response time"):
        threshold = 5
        assert response.elapsed.total_seconds() < threshold, (
            f"Response exceeded {threshold}s"
        )