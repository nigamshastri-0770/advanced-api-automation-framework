import requests


class BookingService:

    BASE_URL = (
        "https://restful-booker.herokuapp.com"
    )

    def create_booking(
        self,
        payload
    ):

        response = requests.post(
            f"{self.BASE_URL}/booking",
            json=payload
        )

        response.raise_for_status()

        return response.json()

    def get_booking(
        self,
        booking_id
    ):

        response = requests.get(
            f"{self.BASE_URL}/booking/{booking_id}"
        )

        response.raise_for_status()

        return response.json()