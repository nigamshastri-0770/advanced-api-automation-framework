import pytest


@pytest.mark.retry
@pytest.mark.regression
def test_retry_logic(
    apis
):

    with pytest.raises(
        Exception
    ):

        apis[
            "jsonplaceholder"
        ].client.get(
            "https://wrong-url.com"
        )