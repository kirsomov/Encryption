import string
import pickle
import alphabet


def get_symbol_pos(symbol):
    return alphabet.DICT_OF_SYMBOLS_WITH_POSITIONS[symbol]


def get_encrypted_symbol(symbol, key_symbol):
    if symbol not in alphabet.DICT_OF_SYMBOLS_WITH_POSITIONS:
        return symbol
    symbol_pos = get_symbol_pos(symbol)
    key_symbol_pos = get_symbol_pos(key_symbol)
    encrypted_symbol_pos = (symbol_pos + key_symbol_pos) % len(alphabet.ALPHABET)
    return alphabet.ALPHABET[encrypted_symbol_pos]


def get_decrypted_symbol(symbol, key_symbol):
    if symbol not in alphabet.DICT_OF_SYMBOLS_WITH_POSITIONS:
        return symbol
    symbol_pos = get_symbol_pos(symbol)
    key_symbol_pos = get_symbol_pos(key_symbol)
    alphabet_length = len(alphabet.ALPHABET)
    decrypted_symbol_pos = (symbol_pos - key_symbol_pos + alphabet_length) % alphabet_length
    return alphabet.ALPHABET[decrypted_symbol_pos]


def encode(text, key):
    return "".join(get_encrypted_symbol(text[i], key[i % len(key)]) for i in range(len(text)))


def decode(text, key):
    return "".join(get_decrypted_symbol(text[i], key[i % len(key)]) for i in range(len(text)))
