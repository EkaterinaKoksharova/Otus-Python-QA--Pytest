import pytest


class TestString:

    poem = """Я помню чудное мгновенье:
              Передо мной явилась ты,
              Как мимолетное виденье,
              Как гений чистой красоты."""

    # Текст должен начинаться со слов
    def test_string_1(self):
        assert self.poem.startswith('Я помню')

    # Текст содержит слова
    def test_string_2(self):
        assert 'Я помню чудное мгновенье' in self.poem

    # Текст не привышает заданную длину символов
    def test_string_3(self):
        assert len(self.poem) <= 153

    # Текст не содержит ругательные слова
    def test_string_4(self, string_params):
        assert string_params in self.poem

    # Текст не содержит ругательные слова
    @pytest.mark.parametrize('bad_words', ['ругательства', 'оскорбления'])
    def test_string_5(self, bad_words):
        assert bad_words in self.poem
