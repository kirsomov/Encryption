import pickle
import string


alphabet = string.ascii_letters


def ShiftSymbol(symbol, shift):
    pos = alphabet.find(symbol)
    pos = (pos + shift) % len(alphabet)
    return alphabet[pos]


def ShiftString(string, shift):
    shifted_string = ""
    for symbol in string:
        if symbol in alphabet:
            shifted_string += ShiftSymbol(symbol, shift)
        else:
            shifted_string += symbol
    return shifted_string


def ShiftText(input_file, output_file, shift):
    with open(input_file) as input_f:
        text = input_f.read()
    with open(output_file, 'w') as output_f:
        output_f.write(ShiftString(text, shift))


def Code(input_file, output_file, key):
    ShiftText(input_file, output_file, key)


def Encode(input_file, output_file, key):
    ShiftText(input_file, output_file, len(alphabet) - key)


def Hack(input_file, symbols_frequency, output_file):
    with open(input_file) as input_f:
        text = input_f.read()
    with open(symbols_frequency, 'rb') as symbols_frequency_f:
        frequency_dict = pickle.load(symbols_frequency_f)
    best_shift = 0
    best_dist = len(alphabet) * len(text)

    for shift in range(len(alphabet)):
        shifted_text = ShiftString(text, shift)
        current_frequency_dict = dict()
        for symbol in alphabet:
            current_frequency_dict[symbol] = 0
        for symbol in shifted_text:
            if symbol in current_frequency_dict:
                current_frequency_dict[symbol] += 1 / len(text)
        current_dist = 0.0
        for symbol in alphabet:
            diff = current_frequency_dict[symbol] - frequency_dict[symbol]
            current_dist += diff * diff
        if current_dist < best_dist:
            best_dist = current_dist
            best_shift = shift

    ShiftText(input_file, output_file, best_shift)
