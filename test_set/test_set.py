import pytest

class TestSet:

    items = {'Петров', 'Сидоров', 'Иванов', 1, 2, 3}
    items2 = ['Петров', 'Петров', 'Сидоров', 'Иванов', 'Иванов', 1, 2, 3]

    # В списке только значения из множества
    def test_set_1(self):
        set_items2 = set(self.items2)
        assert set_items2 == self.items

    # Множество содержит значение
    def test_set_2(self):
        assert 'Петров' in self.items

    # Количество значений в множестве
    def test_set_3(self):
        assert len(self.items) == 6

    # Множество содержит значения
    def test_set_4(self, set_params):
        assert set_params in self.items

    # Множество содержит значения
    @pytest.mark.parametrize('set_params2', ['Петров', 'Цветков', 'Вальхаллов', 1, 2, 3])
    def test_set_5(self, set_params2):
        assert set_params2 in self.items
