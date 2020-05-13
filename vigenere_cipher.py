import string
import pickle
from alphabet import ALPHABET
from alphabet import SYMBOLS_TO_POSITIONS


def encode_symbol(symbol, key_symbol, coefficient):
    """coefficient - параметр, говорящий какая функция вызывается:
    1 для зашифровки, -1 для расшифровки
    encrypted_symbol_pos = (symbol_pos + key_symbol_pos) % len(ALPHABET)
    decrypted_symbol_pos = (symbol_pos - key_cymbol_pos) % len(ALPHABET)
    """
    assert coefficient in [-1, 1], "incorrect coefficient"
    if symbol not in SYMBOLS_TO_POSITIONS:
        return symbol
    symbol_pos = SYMBOLS_TO_POSITIONS[symbol]
    key_symbol_pos = SYMBOLS_TO_POSITIONS[key_symbol]
    return ALPHABET[(symbol_pos + coefficient * key_symbol_pos) % len(ALPHABET)]


def code(text, key, coefficient):
    """coefficient - параметр, говорящий какая функция вызывается:
    1 для зашифровки, -1 для расшифровки
    """
    assert coefficient in [-1, 1], "incorrect coefficient"
    return "".join(encode_symbol(symbol, key[i % len(key)], coefficient) for i, symbol in enumerate(text))


def encode(text, key):
    return code(text, key, 1)


def decode(text, key):
    return code(text, key, -1)
