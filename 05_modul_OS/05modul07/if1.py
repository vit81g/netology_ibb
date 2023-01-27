""" Импорт библиотек """
import sys
import os

""" Условие проверки на принадлежность к директории """
if os.path.isdir(sys.argv[1]):
    print("directory exist")
    
else:
    print("directory not exist")
