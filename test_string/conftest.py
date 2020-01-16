import pytest

@pytest.fixture(params=['ругательства', 'оскорбления'])
def string_params(request):
    return request.param
