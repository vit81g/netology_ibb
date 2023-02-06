# перед началом надо установить библиотеку pycryptodome
# pip install pycryprodome
# импорт модулей
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import ast

# Блоки
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

# Основная фраза
plain_text = 'Secret top'

# Присвоение переменной key хэша от трехзначного числа
key = hashlib.sha256(b"123").digest()

# Вывод значения key
print("key: ", key)

# Шифровка
text = pad(plain_text)
# разбиваем по блокам
iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = (iv + cipher.encrypt(text.encode()))
print("Ciphered text:", cipher_text.hex())

# Расшифровка
unpad = lambda s : s[:-ord(s[len(s)-1:])]
# cipher_text = cipher_text
iv = cipher_text[:BS]

# счетчик для удобства
i = 0

# Brutforce

for l in range(10):             # перебор первого символа от 0 до 9
    for m in range(10):         # перебор второго символа от 0 до 9
        for n in range(10):     # перебор третьего символа от 0 до 9
            i += 1
            # присваеиваем переменной строковыое значение из трех чисел
            new_key = str(l) + str(m) + str(n)
            # преобразование строки в байты
            byte_new_key = new_key.encode('utf-8')
            # преобразуем байты в хэш
            hash_new_key = hashlib.sha256(byte_new_key).digest()
            # вывод счетчика для удобства
            print(i)
            # Расшифровка с учетом перебора трехзначного числового ключа
            cipher = AES.new(hash_new_key, AES.MODE_CBC, iv)
            # Приводим в читаемый вид
            plain_text = unpad(cipher.decrypt(cipher_text[BS:]))
            print(plain_text)
