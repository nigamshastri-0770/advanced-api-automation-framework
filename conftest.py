import pytest

from core.api_client import APIClient
from core.context import Context

from services.reqres_api import ReqResAPI
from services.jsonplaceholder_api import JsonPlaceholderAPI
from services.httpbin_api import HTTPBinAPI
from services.booking_api import BookingAPI


@pytest.fixture(scope="session")
def client():
    return APIClient()


@pytest.fixture(scope="session")
def ctx():
    return Context()


@pytest.fixture
def apis():
    client = APIClient()

    return {
        "booking": BookingAPI(client),
        "reqres": ReqResAPI(client),
        "httpbin": HTTPBinAPI(client),
        "jsonplaceholder": JsonPlaceholderAPI(client)
    }