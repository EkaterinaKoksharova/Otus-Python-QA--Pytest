import pytest

class TestList:

    numbers = [2, 4, 6, 8, 10]

    # Первое значение списка меньше следующего
    def test_list_1(self):
        assert self.numbers[0] < self.numbers[1]

    # Второе значение списка больше предыдущего на 2
    def test_list_2(self):
        assert self.numbers[1] == self.numbers[0] + 2

    # Количество значений списка
    def test_list_3(self):
        assert len(self.numbers) == 5

    # Заданные значения не превышают значения из списка
    def test_list_4(self, list_params):
        assert list_params >= self.numbers[4]

    # Заданные значения не превышают значения из списка
    @pytest.mark.parametrize('numbers_parameters', [10, 12, 14, 16, 18])
    def test_list_5(self, numbers_parameters):
        assert numbers_parameters >= self.numbers[4]
