def validate_booking_exists(
    booking_id,
    db
):

    result = db.execute(
        """
        SELECT id
        FROM bookings
        WHERE id=%s
        """,
        (booking_id,)
    )

    assert len(result) > 0

    return result