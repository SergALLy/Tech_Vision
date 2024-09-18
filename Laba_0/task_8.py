# task_8
# Сумма вводимых чисел
n=input ('Для выхода введите любую букву\n')
sum=0
while n.isdigit(): # Проверка на число
    sum+=int(n)
    n = input()
print('Сумма:',sum)