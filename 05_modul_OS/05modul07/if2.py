""" Импорт библиотек """
import sys
import os

""" Условие проверки на принадлежность к директории """
if os.path.isdir(sys.argv[1]):
    print("directory exist")

# Условие проверки на принадлежность к файлу, если первое условие False   
elif os.path.isfile(sys.argv[1]):
    print("file exist")

# Все условия равны False 
else:
    print("directory not exist")
