import pytest

from validators.contract_validator import (
    validate_contract
)

from schemas.booking_schema import (
    booking_schema
)


@pytest.mark.api
def test_booking_contract(
    apis
):

    payload = {

        "firstname":
        "Nigam",

        "lastname":
        "Shastri",

        "totalprice":
        100,

        "depositpaid":
        True,

        "bookingdates": {

            "checkin":
            "2026-06-18",

            "checkout":
            "2026-06-20"
        }
    }

    response = (

        apis[
            "booking"
        ]

        .create_booking(
            payload
        )
    )

    assert (

        response.status_code

        ==

        200
    )

    validate_contract(
        response,
        booking_schema
    )