from faker import Faker
import random


fake = Faker()


class BookingFactory:

    @staticmethod
    def create():

        return {

            "firstname":
                fake.first_name(),

            "lastname":
                fake.last_name(),

            "totalprice":
                random.randint(
                    100,
                    1000
                ),

            "depositpaid":
                random.choice(
                    [
                        True,
                        False
                    ]
                ),

            "bookingdates": {

                "checkin":
                    "2026-06-16",

                "checkout":
                    "2026-06-18"
            }
        }