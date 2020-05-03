import sys
import argparse


import counting_frequency
import caesar_cipher
import vigenere_cipher


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    parser_hack = subparsers.add_parser('hack')
    parser_hack.add_argument('--cipher', required=True)
    parser_hack.add_argument('--symbols_frequency', required=True)
    parser_hack.add_argument('--input_file')
    parser_hack.add_argument('--output_file')

    parser_counting_frequency = subparsers.add_parser('counting_frequency')
    parser_counting_frequency.add_argument('--input_file')
    parser_counting_frequency.add_argument('--output_file', required=True)

    parser_encode = subparsers.add_parser('encode')
    parser_encode.add_argument('--key', required=True)
    parser_encode.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
    parser_encode.add_argument('--input_file')
    parser_encode.add_argument('--output_file')

    parser_decode = subparsers.add_parser('decode')
    parser_decode.add_argument('--key', required=True)
    parser_decode.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
    parser_decode.add_argument('--input_file')
    parser_decode.add_argument('--output_file')

    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    mode = args.subparser_name
    if args.input_file:
        with open(args.input_file) as input_f:
            input_text = input_f.read()
    else:
        input_text = sys.stdin.read()
    input_text = input_text.strip('\n')
    if mode == "counting_frequency":
        counting_frequency.dump_frequency(input_text, args.output_file)
    else:
        if args.cipher == 'caesar':
            if mode == 'encode':
                output_text = caesar_cipher.encode(input_text, int(args.key))
            elif mode == 'decode':
                output_text = caesar_cipher.decode(input_text, int(args.key))
            elif mode == 'hack':
                output_text = caesar_cipher.hack(input_text, args.symbols_frequency)
        elif args.cipher == 'vigenere':
            if mode == 'encode':
                output_text = vigenere_cipher.encode(input_text, args.key)
            elif mode == 'decode':
                output_text = vigenere_cipher.decode(input_text, args.key)
        if args.output_file:
            with open(args.output_file, 'w') as output_f:
                output_f.write(output_text)
        else:
            print(output_text)
