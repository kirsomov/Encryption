Примеры использования

Подсчёт букв в тексте в frequency.pickle хранится словарь пар символ-частота
python3 main.py counting_frequency --input_file text.txt --output_file symbols_frequency.pickle

Шифрование с помощью шифра Цезаря
python3 main.py code --input_file text.txt --output_file encrypted_text.txt --cipher caesar --key 

Дешифрование шифра Цезаря
python3 main.py encode --input_file encrypted_text.txt --output_file decrypted_text.txt --cipher caesar --key 

Взлом шифра Цезаря
python3 main.py hack --input_file encrypted_text.txt --symbols_frequency symbols_frequency.pickle --output_file decrypted_text.txt --cipher caesar