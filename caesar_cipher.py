import pickle
import string
import math
import alphabet
from collections import defaultdict
import counting_frequency


def shift_symbol(symbol, shift):
    if symbol not in alphabet.DICT_OF_SYMBOLS_WITH_POSITIONS:
        return symbol
    pos = alphabet.DICT_OF_SYMBOLS_WITH_POSITIONS[symbol]
    pos = (pos + shift) % len(alphabet.ALPHABET)
    return alphabet.ALPHABET[pos]


def shift_text(text, shift):
    return "".join(shift_symbol(symbol, shift) for symbol in text)


def encode(input_text, key):
    return shift_text(input_text, key)


def decode(input_text, key):
    return shift_text(input_text, -key)


def hack(input_text, symbols_frequency):
    frequency_dict = counting_frequency.load_frequency(symbols_frequency)
    best_shift = 0
    best_dist = math.inf

    current_frequency_dict = defaultdict(float)

    for symbol in input_text:
        current_frequency_dict[symbol] += 1 / len(input_text)

    for shift in range(len(alphabet.ALPHABET)):
        current_dist = 0.0
        for i in range(len(alphabet.ALPHABET)):
            symbol = alphabet.ALPHABET[i]
            diff = current_frequency_dict.get(alphabet.ALPHABET[i], 0)
            diff -= frequency_dict.get(alphabet.ALPHABET[(i + shift) % len(alphabet.ALPHABET)], 0)
            current_dist += diff ** 2
        if current_dist < best_dist:
            best_dist = current_dist
            best_shift = shift

    return shift_text(input_text, best_shift)


print(hack(";asldkfj", 'frequency.pickle'))
