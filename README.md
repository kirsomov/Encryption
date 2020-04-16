Подсчёт букв в тексте в frequency.pickle хранится словарь пар символ-частота
python main.py counting_frequency --input_file text.txt --output_file symbols_frequency.pickle

Шифрование с помощью шифра Цезаря
python main.py encode --input_file text.txt --output_file encrypted_text.txt --cipher caesar --key <key: number>

Дешифрование шифра Цезаря
python main.py decode --input_file encrypted_text.txt --output_file decrypted_text.txt --cipher caesar --key <key: number>

Взлом шифра Цезаря
python main.py hack --input_file encrypted_text.txt --symbols_frequency symbols_frequency.pickle --output_file decrypted_text.txt --cipher caesar

Шифрование с помощью шифра Виженера
python main.py encode --input_file text.txt --output_file encrypted_text.txt --cipher vigenere --key <key: string>

Дешифрование шифра Виженера
python main.py decode --input_file encrypted_text.txt --output_file decrypted_text.txt --cipher vigenere --key <key: string>