#! /bin/bash

# присвоение переменной значения выполнения команды ls 
list=$(ls)
# задаем переменную i (счетчик)
i=0

# цикл for перебор элемнтов списка list
for mv in $(ls)

do #начало цикла
	echo $mv    # вывод файла
	i=$((i +1)) # запуск счетчика
done

# вывод количества файлов
echo "Total files: $i"
