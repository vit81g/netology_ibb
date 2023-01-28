""" Импорт библиотек """
import os
import sys
import base64

# обявляем переменные
arg1 = sys.argv[1]  # параметр для выбора шифровки или дешифровки
arg2 = sys.argv[2]

# первое условие если параметр равен crypt
if arg1 == 'crypt':
    b_arg2 = arg2.encode("UTF-8") #преобразование строки в байты
    codeBase64_arg2 = base64.b64encode(b_arg2)  # кодируем в base64
    encode_arg2 = codeBase64_arg2.decode("UTF-8")  #преобразование из байтов в UTF-8
    print(encode_arg2)

# второе условие если параметр равен decrypt  
elif arg1 == 'decrypt':
    utf_arg2 = arg2.encode("UTF-8") # преобразование в UTF-8
    decode_utf_arg = base64.b64decode(utf_arg2) # расшифровка base64 байтов 
    decode_arg2 = decode_utf_arg.decode("UTF-8") # преобразование в UTF-8
    print(decode_arg2)
    
# если оба условия не верны
else:
    print ("Неизвестный первый параметр")
