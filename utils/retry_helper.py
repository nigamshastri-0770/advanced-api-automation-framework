import pytest

from utils.retry_helper import (
    retry
)


class MockResponse:

    def __init__(
        self,
        status_code
    ):

        self.status_code = (
            status_code
        )


def test_retry_success_first_attempt():

    @retry()

    def api():

        return (
            MockResponse(
                200
            )
        )

    response = (
        api()
    )

    assert (
        response.status_code
        ==
        200
    )


def test_retry_success_after_retry():

    attempts = [
        0
    ]

    @retry(
        retries=3,
        delay=0
    )

    def api():

        attempts[
            0
        ] += 1

        if (
            attempts[
                0
            ]
            <
            3
        ):

            return (
                MockResponse(
                    503
                )
            )

        return (
            MockResponse(
                200
            )
        )

    response = (
        api()
    )

    assert (
        response.status_code
        ==
        200
    )


def test_retry_limit_exceeded():

    @retry(
        retries=2,
        delay=0
    )

    def api():

        return (
            MockResponse(
                503
            )
        )

    with pytest.raises(
        Exception,
        match="Retry limit exceeded"
    ):

        api()