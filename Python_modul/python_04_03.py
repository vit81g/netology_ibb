# Задание 3
# Дан список поисковых запросов. Получить распределение количества слов в них. 
# Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
#     ]

# Решение
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

# Создаем дополнительные переменные
new_list = []
number_list = []
m = 0

# Первый перебор для создания списка из слов
for i in queries:
    list = i.split()
    new_list.append(list)

# Второй перебор, в котором мы получаем список состоящий из длинн списков
for n in new_list:
    len_list = len(n)
    number_list.append(len_list)
# !!!!
# Более простой вариант от Ярослава, получаем список цифр за один перебор
# for i in queries:
#     list = i.split()
#     number_list.append(len(list))
# !!!!
    
# Вычисляем длинну списка
len_list_all = len(number_list)

# Цикл для вывода значений которые есть в списке - <= max(number_list) получение максимального числа для перебора
while m <= max(number_list):
    # Условие - если количество слов в запросе больше 0, то 
    if number_list.count(m) > 0:
        # Вычисление процентного соотношения
        procent_num = number_list.count(m) / len_list_all *100
        # Преобразование в читаемый вид, два знака после запятой
        a =str(f'{procent_num:.2f}')
        # Вывод решения
        print(f'Запрос из {m} слов - {a}%')
    m +=1
   

