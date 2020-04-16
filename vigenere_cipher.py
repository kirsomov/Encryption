import string
import pickle


alphabet = string.ascii_letters
alphabet += ' '
alphabet += string.punctuation
alphabet += "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def GetVigenereSquare():
    square = list()
    for i in range(len(alphabet)):
        square.append(alphabet[i:]+alphabet[:i])
    return square


square = GetVigenereSquare()


def GetEncryptedSymbol(symbol, key_symbol):
    symbol_pos = alphabet.find(symbol)
    key_symbol_pos = alphabet.find(key_symbol)
    return square[symbol_pos][key_symbol_pos]


def GetDecryptedSymbol(symbol, key_symbol):
    key_symbol_pos = alphabet.find(key_symbol)
    column = square[key_symbol_pos].find(symbol)
    return square[0][column]


def GetEncryptedString(string, key):
    encrypted_string = ""
    key = key*(len(string) // len(key) + 1)
    for symbol, key_symbol in zip(string, key):
        if symbol in alphabet:
            encrypted_string += GetEncryptedSymbol(symbol, key_symbol)
        else:
            encrypted_string += symbol
    return encrypted_string


def GetDecryptedString(string, key):
    decrypted_string = ""
    key = key*(len(string) // len(key) + 1)
    for symbol, key_symbol in zip(string, key):
        if symbol in alphabet:
            decrypted_string += GetDecryptedSymbol(symbol, key_symbol)
        else:
            decrypted_string += symbol
    return decrypted_string


def Encode(input_file, output_file, key):
    with open(input_file) as input_f:
        text = input_f.read()
    with open(output_file, 'w') as output_f:
        output_f.write(GetEncryptedString(text, key))


def Decode(input_file, output_file, key):
    with open(input_file) as input_f:
        text = input_f.read()
    with open(output_file, 'w') as output_f:
        output_f.write(GetDecryptedString(text, key))
