﻿# объявляем переменные
$names = Get-ChildItem  # список каталогов и файлов
$i=0                    # переменная счетик

# foreach цикл для перебора 
foreach($n in $names)

{
    $i+=1               # счетчик увеличивается на единицу
    echo($n.Name)       # вывод на экран с помощью цикла значений списка $names
}

# вывод количества значений в списке
echo ("Total: " + $i)