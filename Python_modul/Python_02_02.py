# Ссылки на задание 
# https://www.hackerrank.com/spellhvit
# https://replit.com/@vit81g/0202python#main.py
# https://replit.com/@vit81g/0203python#main.py



height = 182
age = 25
child_have = 1
study_now = True

if study_now:
    
    if 18 < age < 27:
        
        if child_have < 2:
        
            if height < 170:
                print('В танкисты')

        # это условие сработает и выдаст True и print, после него последующие условия не рассматриваются
            elif height < 185:
                print('На флот')

        # в данном случае это условие не будет выполнено, потому что python выполняет только до первого true, потом все
            elif height < 200:                
                print('Десантники')
            else :
                print('В другие войска')
        else:
            print('Ограничение по детям')
    else:
        print('Непризывной возраст')

else:
    print('Проходит обучение')
