""" Импорт библиотек """
import os
import sys

""" Условие проверки на принадлежность к директории """
if os.path.isdir(sys.argv[1]):
    print("directory exist")

# еще условие по проверки на принадлежность к файлу    
elif os.path.isfile(sys.argv[1]):
    print("file")

# если все условия False
else:
    print("directory not exist")
