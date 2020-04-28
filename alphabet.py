import string


ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET += ALPHABET.upper()
ALPHABET += string.ascii_letters
ALPHABET += ' '
ALPHABET += string.punctuation


DICT_OF_SYMBOLS_WITH_POSITIONS = {symbol: i for i, symbol in enumerate(ALPHABET)}
