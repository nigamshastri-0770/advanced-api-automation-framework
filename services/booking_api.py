from core.config_reader import config


class BookingAPI:

    def __init__(self, client):
        self.client = client
        self.base_url = config["booking"]["base_url"]

    def create_booking(self, payload):
        return self.client.post(
            f"{self.base_url}/booking",
            json=payload
        )