import sys
import argparse

import counting_frequency
import caesar_cipher
import vigenere_cipher


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    parser.add_argument('input_string', nargs='?')
    parser.add_argument('--input_file')
    parser.add_argument('--output_file')
    parser.add_argument('--cipher')
    parser.add_argument('--key')
    parser.add_argument('--symbols_frequency')
    return parser


if __name__ == "__main__":
    assert(len(sys.argv) > 1)
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.input_file:
        with open(namespace.input_file) as input_f:
            input_text = input_f.read()
    else:
        input_text = namespace.input_string
    if namespace.mode == "counting_frequency":
        if namespace.output_file:
            counting_frequency.get_frequency_as_pickle(input_text, namespace.output_file)
        else:
            counting_frequency.print_frequency(input_text)
    else:
        if namespace.cipher == 'caesar':
            if namespace.mode == 'encode':
                output_text = caesar_cipher.encode(input_text, int(namespace.key))
            elif namespace.mode == 'decode':
                output_text = caesar_cipher.decode(input_text, int(namespace.key))
            elif namespace.mode == 'hack':
               output_text = caesar_cipher.hack(input_text, namespace.symbols_frequency)
            else:
                assert(False)
        elif namespace.cipher == 'vigenere':
            if namespace.mode == 'encode':
                output_text = vigenere_cipher.encode(input_text, namespace.key)
            elif namespace.mode == 'decode':
                output_text = vigenere_cipher.decode(input_text, namespace.key)
            else:
                assert(False)
        else:
            assert(False)
        if namespace.output_file:
            with open(namespace.output_file, 'w') as output_f:
                output_f.write(output_text)
        else:
            print(output_text)
