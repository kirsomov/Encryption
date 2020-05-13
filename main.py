import sys
import argparse


import counting_frequency
import caesar_cipher
import vigenere_cipher


# tool for encoding, decoding, conting frequency and hacking
def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='mode', help=" \
            the parser has subparsers: hack, counting_frequency, encode, decode; \
            which are selected depending on the mode \
            all subparsers have arguments --input_file, --output_file, \
            which are optional for all modes except counting_frequency, in which --output_file is required \
            in the absence of these parameters, input and output are carried out through the console ")

    parser_hack = subparsers.add_parser('hack')
    parser_hack.add_argument('--cipher', required=True,
                             help="required argument, caesar or cipher")
    parser_hack.add_argument('--symbols_frequency', required=True,
                             help="required argument")
    parser_hack.add_argument('--input_file',
                             help="if the argument is passed input from a file, else through the console")
    parser_hack.add_argument('--output_file',
                             help="if the argument is passed output from a file, else through the console")

    parser_counting_frequency = subparsers.add_parser('counting_frequency')
    parser_counting_frequency.add_argument('--input_file',
                                           help="if the argument is passed input from a file, else through the console")
    parser_counting_frequency.add_argument('--output_file', required=True,
                                           help="required argument, output through the console")

    parser_encode = subparsers.add_parser('encode')
    parser_encode.add_argument('--key', required=True,
                               help="int in caesar cipher or string in vigenere cipher, required argument")
    parser_encode.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'],
                               help="required argument, caesar or cipher")
    parser_encode.add_argument('--input_file',
                               help="if the argument is passed input from a file, else through the console")
    parser_encode.add_argument('--output_file',
                               help="if the argument is passed output from a file, else through the console")

    parser_decode = subparsers.add_parser('decode')
    parser_decode.add_argument('--key', required=True, help="int in caesar cipher or string in vigenere cipher")
    parser_decode.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'],
                               help="required argument, caesar or cipher")
    parser_decode.add_argument('--input_file',
                               help="if the argument is passed input from a file, else through the console")
    parser_decode.add_argument('--output_file',
                               help="if the argument is passed output from a file, else through the console")

    return parser


def read_input_text(input_file):
    if args.input_file:
        with open(args.input_file) as input_f:
            return input_f.read()
    else:
        return sys.stdin.read()


def print_output_text(output_file, output_text):
    if output_file:
        with open(output_file, 'w') as output_f:
            output_f.write(output_text)
    else:
        print(output_text, end="")


def processing_request(input_text, args):
    if args.mode == "counting_frequency":
        counting_frequency.dump_frequency(input_text, args.output_file)
    else:
        if args.cipher == 'caesar':
            if args.mode == 'encode':
                output_text = caesar_cipher.encode(input_text, int(args.key))
            elif args.mode == 'decode':
                output_text = caesar_cipher.decode(input_text, int(args.key))
            elif args.mode == 'hack':
                output_text = caesar_cipher.hack(input_text, args.symbols_frequency)
        elif args.cipher == 'vigenere':
            if args.mode == 'encode':
                output_text = vigenere_cipher.encode(input_text, args.key)
            elif args.mode == 'decode':
                output_text = vigenere_cipher.decode(input_text, args.key)
        print_output_text(args.output_file, output_text)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    input_text = read_input_text(args.input_file)
    processing_request(input_text, args)
