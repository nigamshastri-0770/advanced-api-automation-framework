import pytest


@pytest.mark.api
def test_headers_exist(
    apis
):

    response = (

        apis[
            "httpbin"
        ]

        .get_headers()

    )

    if (

        response.status_code

        ==

        503

    ):

        pytest.skip(

            "HTTPBin unavailable"

        )

    assert (

        response.status_code

        ==

        200

    )

    assert (

        "headers"

        in

        response.json()

    )