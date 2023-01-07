# Задание 4
# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# Решение
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# Находим максимальное значение из всех значений (values()) словаря
max_value = max(stats.values())

# Перебор ключей (key) и значений ключей (vars)
for key, vars in stats.items():
    # Сравнение значения ключей с максимальным значением max_value
    if vars == max_value:
        # Вывод на экран
        print(key)


