import pytest

class TestDictionary:

    flowers = {'Тюльпаны': 'желтые', 'Розы': 'розовые', 'Калы': 'белые'}

    # Ключу в словаре соответствует значение
    def test_dict_1(self):
        assert self.flowers['Тюльпаны'] == 'желтые'

    # Количество записей в словаре
    def test_dict_2(self):
        assert len(self.flowers.items()) == 3

    # Количество значений в словаре
    def test_dict_3(self):
        assert len(self.flowers) == 3

    # В списке значений словаря содержатся значения
    def test_dict_4(self, dict_params):
        assert dict_params in self.flowers.values()

    # В списке ключей словаря содержатся значения
    @pytest.mark.parametrize('dict_params2', ['Фиалки', 'Тюльпаны', 'Розы', 'Калы'])
    def test_dict_5(self, dict_params2):
        assert dict_params2 in self.flowers.keys()
