import pytest

@pytest.fixture(params=['розовые', 'желтые', 'зеленые', 'белые'])
def dict_params(request):
    return request.param
