import json
import allure


def attach_request(
    payload
):

    allure.attach(

        json.dumps(
            payload,
            indent=4
        ),

        name="Request Payload",

        attachment_type=
        allure.attachment_type.JSON
    )


def attach_response(
    response
):

    allure.attach(

        response.text,

        name="Response",

        attachment_type=
        allure.attachment_type.JSON
    )


def attach_execution_time(
    response
):

    allure.attach(

        f"{response.elapsed.total_seconds()} sec",

        name="Execution Time"

    )