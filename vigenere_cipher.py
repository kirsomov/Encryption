import string
import pickle


ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET += ALPHABET.upper()
ALPHABET += string.ascii_letters
ALPHABET += ' '
ALPHABET += string.punctuation


DICT_OF_SYMBOLS_WITH_POSITIONS = {ALPHABET[i]: i for i in range(len(ALPHABET))}


def get_vigenere_square():
    square = list()
    for i in range(len(ALPHABET)):
        square.append(ALPHABET[i:]+ALPHABET[:i])
    return square


SQUARE = get_vigenere_square()


def get_encrypted_symbol(symbol, key_symbol):
    if not symbol in DICT_OF_SYMBOLS_WITH_POSITIONS:
        return symbol
    symbol_pos = ALPHABET.find(symbol)
    key_symbol_pos = ALPHABET.find(key_symbol)
    return SQUARE[symbol_pos][key_symbol_pos]


def get_decrypted_symbol(symbol, key_symbol):
    if not symbol in DICT_OF_SYMBOLS_WITH_POSITIONS:
        return symbol
    key_symbol_pos = ALPHABET.find(key_symbol)
    column = SQUARE[key_symbol_pos].find(symbol)
    return ALPHABET[column]


def encode(text, key):
    return "".join(get_encrypted_symbol(symbol, key) for symbol in text)


def decode(text, key):
    return "".join(get_decrypted_symbol(symbol, key) for symbol in text)
