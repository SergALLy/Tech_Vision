# task_5
# Последовательность Фибоначчи
n = int(input())
a=1
b=0
print(0, end=" ")
for i in range(1,n):
    print(a, end=" ")
    a, b = a+b, a # Вычисление нового члена последовательности