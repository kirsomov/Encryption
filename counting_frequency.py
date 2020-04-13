import pickle


def GetFrequency(input_file, output_file):
    with open(input_file, 'r') as input_f:
        text = input_f.read()
    frequency_dict = dict()
    for symbol in text:
        if symbol in frequency_dict:
            frequency_dict[symbol] += 1 / len(text)
        else:
            frequency_dict[symbol] = 1 / len(text)
    with open(output_file, 'wb') as output_f:
        pickle.dump(frequency_dict, output_f)
