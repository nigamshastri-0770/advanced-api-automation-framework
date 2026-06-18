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


def test_api_db_validation():

    service = BookingService()

    payload = booking_payload()

    booking = (
        service.create_booking(
            payload
        )
    )

    booking_id = (
        booking[
            "bookingid"
        ]
    )

    db = Database(
        host="localhost",
        database="api",
        user="macbookpro",
        password=""
    )

    # Insert simulated API result
    db.execute(
        """
        INSERT INTO bookings(id)
        VALUES(%s)
        ON CONFLICT DO NOTHING
        """,
        (booking_id,)
    )

    db.connection.commit()

    validate_booking_exists(
        booking_id,
        db
    )

    db.close()