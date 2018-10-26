import pytest

from backend.factory import create_app


@pytest.fixture
def test_app():
    test_app = create_app('testing')
    return test_app
