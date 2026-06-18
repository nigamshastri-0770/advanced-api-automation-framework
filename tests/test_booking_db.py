import os
import pytest

from core.database import Database
from validators.db_validator import (
    validate_booking_exists
)


@pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="Skip DB tests in CI"
)
def test_booking_db_validation():

    db = Database(
        host="localhost",
        database="api",
        user="macbookpro",
        password=""
    )

    validate_booking_exists(
        1,
        db
    )

    db.close()