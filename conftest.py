import pytest

def pytest_addoption(parser):
    parser.addoption("--driverName", action="store", default="chrome")

@pytest.fixture
def driverName(request):
    return request.config.getoption("--driverName")