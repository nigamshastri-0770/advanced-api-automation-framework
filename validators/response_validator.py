def validate_json(response):
    try:
        data = response.json()
        return data is not None
    except Exception:
        raise AssertionError("Response is not valid JSON")


def validate_keys(response, required_keys):
    data = response.json()

    missing_keys = [key for key in required_keys if key not in data]

    assert not missing_keys, (
        f"Missing keys: {missing_keys}"
    )