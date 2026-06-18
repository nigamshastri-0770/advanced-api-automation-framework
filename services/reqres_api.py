from core.config_reader import config


class ReqResAPI:

    def __init__(
        self,
        client
    ):

        self.client = client

        self.base_url = (
            config[
                "reqres"
            ][
                "base_url"
            ]
        )

    def login(
        self
    ):

        payload = {

            "email":
            "eve.holt@reqres.in",

            "password":
            "cityslicka"
        }

        headers = {
            "x-api-key":
            "free_user_3EqwNfJjHbaSI4VWRBchJllgjn9"
        }

        return (
            self.client.post(
                f"{self.base_url}/login",
                json=payload,
                headers=headers
            )
        )