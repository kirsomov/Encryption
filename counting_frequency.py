import pickle
from collections import defaultdict


def get_frequency_dict(input_string):
    frequency_dict = defaultdict(float)
    for symbol in input_string:
        frequency_dict[symbol] += 1 / len(input_string)
    return frequency_dict


def dump_dict(dictionary, output_file):
    with open(output_file, 'wb') as output_f:
        pickle.dump(dictionary, output_f)


def dump_frequency(input_string, output_file):
    dump_dict(get_frequency_dict, output_file)


def load_frequency(symbols_frequency):
    with open(symbols_frequency, 'rb') as symbols_frequency_f:
        return pickle.load(symbols_frequency_f)
