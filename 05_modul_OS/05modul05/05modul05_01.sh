#! /bin/bash

# задаем первую переменную
var=1
# задаем вторую переменную и присваиваем ей значение дополнительного параметра
agr=$1

# вывод первого задания
echo $agr$var
# вывод второго задания
echo $(($agr + 1))



