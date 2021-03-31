import string


ALPHABET = string.ascii_letters
ALPHABET += ' '
ALPHABET += string.punctuation


RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RUSSIAN_ALPHABET += RUSSIAN_ALPHABET.upper()


ALPHABET += RUSSIAN_ALPHABET


SYMBOLS_TO_POSITIONS = {symbol: i for i, symbol in enumerate(ALPHABET)}
