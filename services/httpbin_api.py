import requests


class HTTPBinAPI:

    def __init__(
        self,
        client
    ):

        self.client = client

    def get_headers(self):

        try:

            return self.client.get(
                "https://httpbin.org/headers"
            )

        except requests.exceptions.HTTPError:

            class FakeResponse:

                status_code = 503

                def json(self):

                    return {
                        "headers": {}
                    }

            return FakeResponse()