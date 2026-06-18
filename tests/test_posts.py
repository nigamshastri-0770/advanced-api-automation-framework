import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_fetch_posts(apis):

    response = (
        apis["jsonplaceholder"]
        .get_posts()
    )

    assert (
        response.status_code
        ==
        200
    )

    posts = (
        response.json()
    )

    assert (
        len(posts)
        >
        0
    )