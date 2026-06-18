import time
import requests

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

from utils.logger import Logger


class APIClient:

    def __init__(self):

        self.session = (
            requests.Session()
        )

        self.logger = (
            Logger.get_logger()
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=2,
            min=1,
            max=3,
        ),
        retry=retry_if_exception_type(
            (
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.HTTPError
            )
        ),
        reraise=True
    )
    def get(
        self,
        url,
        headers=None,
        params=None
    ):

        start = time.time()

        try:

            self.logger.info(
                f"GET → {url}"
            )

            response = (
                self.session.get(
                    url,
                    headers=headers,
                    params=params,
                    timeout=30
                )
            )

            execution = (
                time.time()
                -
                start
            )

            self.logger.info(
                f"Status → {response.status_code}"
            )

            self.logger.info(
                f"Execution → {execution:.2f}s"
            )

            # Retry only server failures
            if (
                response.status_code
                >=
                500
            ):

                raise (
                    requests.exceptions.HTTPError(
                        f"{response.status_code}"
                    )
                )

            return response

        except Exception as e:

            self.logger.error(
                f"Retry Triggered → {str(e)}"
            )

            raise

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=2,
            min=1,
            max=10
        ),
        retry=retry_if_exception_type(
            (
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.HTTPError
            )
        ),
        reraise=True
    )
    def post(
        self,
        url,
        json=None,
        headers=None
    ):

        start = time.time()

        try:

            self.logger.info(
                f"POST → {url}"
            )

            self.logger.info(
                f"Payload → {json}"
            )

            response = (
                self.session.post(
                    url,
                    json=json,
                    headers=headers,
                    timeout=30
                )
            )

            execution = (
                time.time()
                -
                start
            )

            self.logger.info(
                f"Status → {response.status_code}"
            )

            self.logger.info(
                f"Execution → {execution:.2f}s"
            )

            # Retry only 5xx
            if (
                response.status_code
                >=
                500
            ):

                raise (
                    requests.exceptions.HTTPError(
                        f"{response.status_code}"
                    )
                )

            return response

        except Exception as e:

            self.logger.error(
                f"Retry Triggered → {str(e)}"
            )

            raise