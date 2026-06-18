import pytest

from utils.data_factory import (
    BookingFactory
)


@pytest.mark.parallel

def test_create_booking_parallel(
    apis
):

    payload = (
        BookingFactory.create()
    )

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