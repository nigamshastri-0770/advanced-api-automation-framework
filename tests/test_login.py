import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_login_success(apis):

    response = (
        apis["reqres"]
        .login()
    )

    assert (
        response.status_code
        ==
        200
    )

    assert (
        "token"
        in
        response.json()
    )


@pytest.mark.regression
@pytest.mark.api
def test_login_invalid_credentials(
    apis
):

    response = (
        apis[
            "reqres"
        ]
        .client
        .post(
            "https://reqres.in/api/login",
            json={
                "email":
                "wrong@test.com",
                "password":
                "wrong"
            },
            headers={
                "x-api-key":
                "reqres-free-v1"
            }
        )
    )

    assert (
        response.status_code
        ==
        401
    )