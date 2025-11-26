import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# TEST capitalize()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('skypro', 'Skypro'),
    ('hello world', 'Hello world'),
    ('python', 'Python'),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('123abc', '123abc'),      # первая буква не буква
    ('', ''),                  # пустая строка
    ('   ', '   '),            # строка из пробелов
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# TEST trim()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('  skypro', 'skypro'),
    ('  hello world', 'hello world'),
    ('python', 'python'),
    ('  123', "123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('', ''),                  # пустая строка
    (' ', ''),                 # один пробел → должен стать пустой строкой
    ('   ', ''),               # только пробелы → должно удалиться всё
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# TEST contains()


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol', [
    ('SkyPro', 'S'),
    ('hello', 'o'),
    ('12345', '3'),
    ('hello world', ' '),          # проверка пробела
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol', [
    ('SkyPro', 'U'),
    ('hello', 'x'),
    ('12345', '9'),
    ('', 'a'),                   # пустая строка ничего не содержит
])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False

# TEST delete_symbol()


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('SkyPro', 'k', 'SyPro'),
    ('SkyPro', 'Pro', 'Sky'),
    ('hello', 'l', 'heo'),
    ('123123', '3', '1212'),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, expected', [
    ('SkyPro', 'X', 'SkyPro'),   # удалять нечего
    ('', 'a', ''),               # пустая строка
    ('hello', '\n', 'hello'),    # удаление управляющего символа
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
