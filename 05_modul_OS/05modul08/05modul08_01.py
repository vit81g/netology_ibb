# импорт библиотек
import nmap3

# обявляем (создаем) объект nmap3.NmapScanTechniques()
nmap = nmap3.NmapScanTechniques()

# присваиваем переменной result значение сканирование объекта с параметрами scan_top_ports("10.0.2.15", args="-sV")
result = nmap.scan_top_ports("10.0.2.15", args="-sV")

# цикл перебора JSON
for i in result['10.0.2.15']['ports']:
    # обработка ошибки  
    try:
       print(i['service']['name'], i['service']['version'], i['portid'])
    
    # обработка ошибки отсутствия ключа в словаре KeyError
    except KeyError:
        print(i['service']['name'], i['portid'])
