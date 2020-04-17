Подсчёт букв в тексте в frequency.pickle хранится словарь пар символ-частота
python main.py counting_frequency <--input_file text.txt OR text> <--output_file symbols_frequency.pickle OR nothing>

Шифрование/дешифрование с помощью шифра Цезаря/Виженера
python main.py <encode OR decode> <--input_file text.txt OR text> <--output_file encrypted_text.txt OR nothing> --cipher <caesar OR vigener> --key <number(ceaser) OR string(vigenere)>

Взлом шифра Цезаря
python main.py hack <--input_file encrypted_text.txt OR text> --symbols_frequency symbols_frequency.pickle <--output_file decrypted_text.txt OR noting> --cipher caesar
