import pickle


def get_frequency_dict(input_string):
    frequency_dict = dict()
    for symbol in input_string:
        if symbol in frequency_dict:
            frequency_dict[symbol] += 1 / len(input_string)
        else:
            frequency_dict[symbol] = 1 / len(input_string)
    return frequency_dict


def get_frequency_as_pickle(input_string, output_file):
    with open(output_file, 'wb') as output_f:
        pickle.dump(get_frequency_dict(input_string), output_f)


def print_frequency(input_string):
    print(get_frequency_dict(input_string))
