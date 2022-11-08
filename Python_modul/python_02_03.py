from datetime import date


month = input('Введите месяц: ')
day = int(input('Введите число: '))

if (month == 'март' and day >=21) or (month == 'апрель' and day <= 20):
    print('Овен')

elif (month == 'апрель' and day >=21) or (month == 'май' and day <= 21):
    print('Телец')

elif (month == 'май' and day >=22) or (month == 'июнь' and day <= 21):
    print('Близнецы')
    
elif (month == 'июнь' and day >=22) or (month == 'июль' and day <= 22):
    print('Рак')
    
elif (month == 'июль' and day >=23) or (month == 'август' and day <= 21):
    print('Лев')
    
elif (month == 'август' and day >=22) or (month == 'сентябрь' and day <= 23):
    print('Дева')
    
elif (month == 'сентябрь' and day >=24) or (month == 'октябрь' and day <= 23):
    print('Весы')

elif (month == 'октябрь' and day >=24) or (month == 'ноябрь' and day <= 22):
    print('Скорпион')
    
elif (month == 'ноябрь' and day >=23) or (month == 'декабрь' and day <= 22):
    print('Стрелец')
    
elif (month == 'декабрь' and day >=23) or (month == 'январь' and day <= 20):
    print('Козерог')
    
elif (month == 'январь' and day >=21) or (month == 'февраль' and day <= 19):
    print('Водолей')
    
elif (month == 'февраль' and day >=20) or (month == 'март' and day <= 20):
    print('Рыбы')

else:
    print('Неверно указана дата')