import pickle
from collections import defaultdict


def get_frequency_dict(input_string):
    frequency_dict = defaultdict(float)
    for symbol in input_string:
        frequency_dict[symbol] += 1 / len(input_string)
    return frequency_dict


def dump_frequency(input_string, output_file):
    with open(output_file, 'wb') as output_f:
        pickle.dump(get_frequency_dict(input_string), output_f)


def load_frequency(symbols_frequency):
    with open(symbols_frequency, 'rb') as symbols_frequency_f:
        return pickle.load(symbols_frequency_f)
