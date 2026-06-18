from jsonschema import (
    validate
)


def validate_contract(
    response,
    schema
):

    if hasattr(
        response,
        "json"
    ):

        response = (
            response.json()
        )

    validate(

        instance=response,

        schema=schema
    )

    return True