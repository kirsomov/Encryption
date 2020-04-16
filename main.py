import sys
import argparse

import counting_frequency
import caesar_cipher
import vigenere_cipher


def CreateParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    parser.add_argument('--input_file')
    parser.add_argument('--output_file')
    parser.add_argument('--cipher')
    parser.add_argument('--key')
    parser.add_argument('--symbols_frequency')
    return parser


if __name__ == "__main__":
    assert(len(sys.argv) > 1)
    parser = CreateParser()
    namespace = parser.parse_args(sys.argv[1:6])
    if namespace.mode == "counting_frequency":
        assert(len(sys.argv) == 6)
        counting_frequency.GetFrequency(namespace.input_file, namespace.output_file)
    else:
        assert(len(sys.argv) == 10)
        namespace = parser.parse_args(sys.argv[1:])
        if namespace.cipher == 'caesar':
            if namespace.mode == 'encode':
                caesar_cipher.Encode(namespace.input_file, namespace.output_file, int(namespace.key))
            elif namespace.mode == 'decode':
                caesar_cipher.Decode(namespace.input_file, namespace.output_file, int(namespace.key))
            elif namespace.mode == 'hack':
                caesar_cipher.Hack(namespace.input_file, namespace.symbols_frequency, namespace.output_file)
            else:
                assert(False)
        elif namespace.cipher == 'vigenere':
            if namespace.mode == 'encode':
                vigenere_cipher.Encode(namespace.input_file, namespace.output_file, namespace.key)
            elif namespace.mode == 'decode':
                vigenere_cipher.Decode(namespace.input_file, namespace.output_file, namespace.key)
            else:
                assert(False)
        else:
            assert(False)
