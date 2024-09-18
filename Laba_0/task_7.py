# task_7
# Поиск всех простыз чисел
n=int(input())
for i in range(2,n+1):
    for k in range(2, i // 2 + 1):
        if i % k == 0:
            break
    else: # Если цикл отработал полностью, то выполняем else
        print(i) 