import sys
import argparse


import counting_frequency
import caesar_cipher
import vigenere_cipher


# у парсера есть разделеня на сабпарсеры: hack, counting_frequency, encode, decode;
# которые выбираются в зависимости от режима
#
# у всех сабпарсеров есть аргументы --input_file, --output_file,
# являющиеся необязательными для всех режимов, кроме counting_frequency, в котором --output_file обязателен
# при отсутствии этих параметров ввод и ввывод осуществляются через консоль
#
# в режимах code, encode параметры --key --cipher также является обязательным
# в шифре Цезаря ключ должен быть числомб в шифре Виженера - строкой
#
# в режиме hack также указываются такие обязательные параметры, как
# шифр (в данной реализации только caesar) и файл с частотами символов
def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='mode')

    parser_hack = subparsers.add_parser('hack')
    parser_hack.add_argument('--cipher', required=True)
    parser_hack.add_argument('--symbols_frequency', required=True)
    parser_hack.add_argument('--input_file')
    parser_hack.add_argument('--output_file')

    parser_counting_frequency = subparsers.add_parser('counting_frequency')
    parser_counting_frequency.add_argument('--input_file')
    parser_counting_frequency.add_argument('--output_file', required=True)

    parser_encode = subparsers.add_parser('encode')
    parser_encode.add_argument('--key', required=True, help="int in caesar cipher or string in vigenere cipher")
    parser_encode.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
    parser_encode.add_argument('--input_file')
    parser_encode.add_argument('--output_file')

    parser_decode = subparsers.add_parser('decode')
    parser_decode.add_argument('--key', required=True, help="int in caesar cipher or string in vigenere cipher")
    parser_decode.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
    parser_decode.add_argument('--input_file')
    parser_decode.add_argument('--output_file')

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
