#  task_9
# Элементы списка
list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
sum=0
for i in list:
    if i<30 and i%3==0:
        print (i, end="\t")
    else: 
        sum+=i
print('\nСумма:',sum)
