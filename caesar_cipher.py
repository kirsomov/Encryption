import pickle
import string


ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET += ALPHABET.upper()
ALPHABET += string.ascii_letters
ALPHABET += ' '
ALPHABET += string.punctuation


DICT_OF_SYMBOLS_WITH_POSITIONS = {ALPHABET[i]: i for i in range(len(ALPHABET))}


def shift_symbol(symbol, shift):
    if symbol not in DICT_OF_SYMBOLS_WITH_POSITIONS:
        return symbol
    pos = DICT_OF_SYMBOLS_WITH_POSITIONS[symbol]
    pos = (pos + shift) % len(ALPHABET)
    return ALPHABET[pos]


def shift_text(text, shift):
    return "".join(shift_symbol(symbol, shift) for symbol in text)


def encode(input_text, key):
    return shift_text(input_text, key)


def decode(input_text, key):
    return shift_text(input_text, -key)


def hack(input_text, symbols_frequency):
    with open(symbols_frequency, 'rb') as symbols_frequency_f:
        frequency_dict = pickle.load(symbols_frequency_f)
    best_shift = 0
    best_dist = len(ALPHABET) * len(input_text)

    for shift in range(len(ALPHABET)):
        shifted_text = shift_text(input_text, shift)
        current_frequency_dict = dict()
        for symbol in ALPHABET:
            if not (symbol in frequency_dict.keys()):
                frequency_dict[symbol] = 0
            current_frequency_dict[symbol] = 0
        for symbol in shifted_text:
            if symbol in current_frequency_dict:
                current_frequency_dict[symbol] += 1 / len(input_text)
        current_dist = 0.0
        for symbol in ALPHABET:
            diff = current_frequency_dict[symbol] - frequency_dict[symbol]
            current_dist += diff * diff
        if current_dist < best_dist:
            best_dist = current_dist
            best_shift = shift

    return shift_text(input_text, best_shift)
