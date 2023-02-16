"""
Задача №2

    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или
    переместить документ на несуществующую полку;
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
    Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

"""

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
def funcDeleteNomber():
    """
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
    :return: documents
    """
    delNumber = input('Введите номер документа: ')
    for i in documents:
        if i['number'] == delNumber:
             documents.remove(i)
        else:
            print('Документв с таким номером не существует')
            break

    return f'{documents}'



def funcMoveNumber():
    """
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или
    переместить документ на несуществующую полку;
    :return: directories
    """
    doc_number = input('Введите номер документа: ')
    new_directories = input('Введите новую полку, куда переместить документ: ')
    if new_directories in directories.keys():
        for i in documents:
            if i['number'] == doc_number:
                new_list = []

            # добавление элемента во временную переменную
                new_list.append(doc_number)
                # print('перебор k')
                for k in directories:
                    # удаление элемента
                    if doc_number in directories[k]:
                        directories[k].remove(doc_number)
                # новый элемент в словаре
                directories[new_directories] = new_list
    else:
        print("такой полки не существует")


    return f'{directories}'

def funcAddDirectories():
    """
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
    Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
    :return:
    """

    new_directories = input('Введите новую полку: ')
    if new_directories in directories.keys():
        print('Полка с таким номером уже существует')

    else:
        directories[new_directories] = []

    return f'{directories}'

if inputCommand == 'd':
    print(funcDeleteNomber())

if inputCommand == 'm':
    print(funcMoveNumber())

if inputCommand == 'as':
    print(funcAddDirectories())


else:
    print("Не верная комманда")
