# task_5
# Последовательность Фибоначчи
n = int(input())
a=1
b=0
if n==1: print(0)
elif n==2: print(1)
else:
    for i in range(2,n):
        a, b = a+b, a # Вычисление нового члена последовательности
    print(a)