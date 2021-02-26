import os
import string
import getpass


def Gamma():
    A = 7
    B = 3
    M = 4096
    y = 2020
    gamma_list = []
    for i in range(8):
        y = (A * y) % M
        gamma_list.append(y)
    return gamma_list


def Coded(text):
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(tt)
    
    text = text.upper().replace(' ', '')
    
    A = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' * 2
    key = getpass.getpass('Введите ключ: ')
    key *= len(text) // len(key) + 1
    permutation = ''.join([A[A.index(j) + int(key[i]) * 1]
                           for i, j in enumerate(text)])
    text = permutation
    
    coded_text = ''
    gamma_list = Gamma()
    cnt = 0
    for i in range(len(text)):
        coded_text += chr((ord(text[i]) + gamma_list[cnt] % 32))
        cnt += 1
        if cnt == 7:
            cnt = 0
    return coded_text


def DeCoded(text):
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(tt)
    
    text = text.replace(' ', '')
    
    decoded_text = ''
    gamma_list = Gamma()
    cnt = 0
    for i in range(len(text)):
        decoded_text += chr((ord(text[i]) - gamma_list[cnt] % 32))
        cnt += 1
        if cnt == 7:
            cnt = 0
    
    A = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' * 2 
    key = getpass.getpass('Введите ключ: ')
    key *= len(decoded_text) // len(key) + 1
    permutation = ''.join([A[A.index(j) + int(key[i]) * (-1)]
                           for i, j in enumerate(decoded_text)])
    decoded_text = permutation
    return decoded_text.lower()


print("1 - Шифрование")
print("2 - Расшифровка")
answer = int(input('Ваш выбор: '))
os.system('CLS')
if answer == 1:
    file_name = input('Введите имя файла (с расширением): ')
    f = open(file_name, 'r', encoding='utf-8')
    text = f.read()
    Coded_message = Coded(text)
    f.close()
    f = open('Coded.txt', 'w', encoding='utf-8')
    f.write(Coded_message)
    f.close()
    print('Файл зашифрован')
    a = input('Нажмите Enter для выхода')

if answer == 2:
    f = open('Coded.txt', 'r', encoding='utf-8')
    text = f.read()
    DeCoded_message = DeCoded(text)
    f.close()
    f = open('DeCoded.txt', 'w', encoding='utf-8')
    f.write(DeCoded_message)
    f.close()
    print('Файл расшифрован')
    a = input('Нажмите Enter для выхода')
