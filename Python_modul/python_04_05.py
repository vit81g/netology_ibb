# Задание 5
# *Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
# (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

# Решение

list_dict = ['2018-01-01', 'yandex', 'cpc', 100]
len_list = len(list_dict) - 1
i = 0
var1_dict = {}

while i < len_list:
    var1_dict.setdefault(list_dict[i], list_dict[i+1])
    i += 1

dict_len = len(var1_dict.keys()) - 1
while dict_len > 0:
    # print(var1_dict)
    var1_dict[list(var1_dict.keys())[dict_len-1]] = {list(var1_dict.keys())[dict_len] : list(var1_dict.values())[dict_len]}
    del(var1_dict[list(var1_dict.keys())[dict_len]])
    dict_len = dict_len - 1;

print(var1_dict)
