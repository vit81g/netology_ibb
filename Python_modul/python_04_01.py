# Задание 1
# Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs,
# содержащий только визиты из России."
# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]

# Решение

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# Создаем дополнительные переменные
geo_logs_len = len(geo_logs) # длинна списка
i = 0                        # переменная шага в цикле
new_geo_logs = []            # новый список (пустой) 
new_dict = {}                # новый словарь (пустой)

# Цикл с учетом длинны списка geo_logs_len
while i < geo_logs_len:
    # Итерация по словарю с выводом значения ключа
    for country in geo_logs[i].values():
        # Проверка на условие - значение ключа должно быть равно 'Россия'
        if country[1] == 'Россия':
            # Присвоение i-го элемента в пустой словарь 
            new_dict = geo_logs[i]
            # Добавление в пустой список значение словаря
            new_geo_logs.append(new_dict)
    # шаг в цикле +1        
    i += 1

# Вывод решения
print(new_geo_logs)



