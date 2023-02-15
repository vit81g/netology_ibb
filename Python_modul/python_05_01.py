"""
Домашнее задание к лекции 5.«Функции — использование встроенных и создание собственных»
Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
      documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
Перечень полок, на которых находятся документы хранится в следующем виде:
      directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
Задача №1
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
"""

# обявление переменных
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# ввод данных для дальнейшей обработки
inputCommand = input("Выберите действие: ")

# Основные функции
def resultNumberName():
    """
    Выполняет извлечение из словаря данных по заданному условию:
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    :param command:
    :return:
    """
    new_list = []
    numbers = input("Введите номер документа: ")
    for i in documents:
        for k in i:
            # print(k)
            if i[k] in numbers:
                new_list.append(i['name'])
    return f'Имя человека: {" ".join(new_list)}'


def resultNumberDicrectories():
    """
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
    :return:
    """
    new_list = []
    numbers = input("Введите номер документа: ")
    for i in directories:
        # print(directories.get(i))
        for k in directories.get(i):
            if k == numbers:
                new_list.append(i)
    return f"Номер полки: {' '.join(new_list)}"


def resultListDoc():
    """
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    :return:
    """
    for i in documents:
        if i['type'] == 'passport':
            return f'{i["type"]} "{i["number"]}" "{i["name"]}"'


def resultAddDoc():
    """
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.
    :return:
    """
    type_dict = input('Введите тип документа: ')
    number_dict = input('Введите номер документа: ')
    name_dict = input('Введите ФИО: ')
    new_dict = {}
    new_dict['type'] = type_dict
    new_dict['number'] = number_dict
    new_dict['name'] = name_dict
    documents.append(new_dict)
    # print(documents)
    number_directories = input('Введите номер полки: ')
    if number_directories in directories.keys():
        new_list = directories[number_directories]
        new_list.append(number_dict)
        directories[number_directories] = new_list

    else:
        print("Такой полки не существует")
        documents.pop(-1)


    return f'{documents} \n {directories}'


# тело программы, обрабатываются вводимые комманды и запускаются функции
if inputCommand == 'p':
    print(resultNumberName())

if inputCommand == 's':
    print(resultNumberDicrectories())

if inputCommand == 'l':
    print(resultListDoc())

if inputCommand == 'a':
    print(resultAddDoc())

