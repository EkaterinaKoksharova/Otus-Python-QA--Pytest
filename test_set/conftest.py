import pytest

@pytest.fixture(params=['Петров', 'Цветков', 'Вальхаллов', 1, 2, 3])
def set_params(request):
    return request.param
