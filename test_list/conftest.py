import pytest

@pytest.fixture(params=[10, 12, 14, 16, 18])
def list_params(request):
    return request.param
