import os
import pytest


@pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="Skip DB integration in CI"
)
def test_api_db_validation():

    from services.booking_service import (
        BookingService
    )

    from data.booking_factory import (
        booking_payload
    )

    from core.database import (
        Database
    )

    from validators.db_validator import (
        validate_booking_exists
    )

    service = BookingService()

    payload = booking_payload()

    booking = (
        service.create_booking(
            payload
        )
    )

    booking_id = booking[
        "bookingid"
    ]

    db = Database(
        host="localhost",
        database="api",
        user="macbookpro",
        password=""
    )

    validate_booking_exists(
        booking_id,
        db
    )

    db.close()