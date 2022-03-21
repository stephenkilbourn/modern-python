from unittest.mock import Mock

from _pytest.config import Config
import pytest
from pytest_mock import MockFixture


def pytest_configure(config: Config) -> None:
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Testing Title",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock
