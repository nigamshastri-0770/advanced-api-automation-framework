from faker import Faker


fake = Faker()


def booking_payload():

    return {

        "firstname":
        fake.first_name(),

        "lastname":
        fake.last_name(),

        "totalprice":
        fake.random_int(
            100,
            1000
        ),

        "depositpaid":
        True,

        "bookingdates": {

            "checkin":
            "2026-06-18",

            "checkout":
            "2026-06-20"
        },

        "additionalneeds":
        "Breakfast"
    }