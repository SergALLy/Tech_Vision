# task_6
# Проверка на палиндром
str = input()
str=str.lower() # Приводим к нижнему регистру
str=str.replace(' ','') # Удаляем все пробелы
str_rev = ''.join(reversed(str)) # Переворачиваем строку
if str==str_rev:
    print('Палиндром')
else:
     print('Не палиндром')