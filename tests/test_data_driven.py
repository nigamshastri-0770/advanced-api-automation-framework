import pytest


@pytest.mark.parametrize(
    "post_id",
    [
        1,
        2,
        3,
        4,
        5
    ]
)
def test_multiple_posts(
    apis,
    post_id
):

    response = (
        apis["jsonplaceholder"]
        .get_post(
            post_id
        )
    )

    assert (
        response.status_code
        ==
        200
    )

    assert (
        response.json()["id"]
        ==
        post_id
    )