# task_1
# Игра Виселица
import random
words = ['игра','слон','окно','кино']
word = random.choice(words)
guesses='*'*len(word)
max_attempts = len(word)+3
attempt = 0
while (attempt<max_attempts):
    print('Угадай слово:', guesses)
    letter = input('Введите букву: ')
    if len(letter)==1: # Проверка на ввод одной буквы
        for i in range(0,len(word)): # цЦкл по всем символам
            if letter [0]==word[i]: # Проверка на совпадение
                guesses_list = list(guesses) # Перевод строки в массив
                guesses_list[i] = letter[0] # Замена символа
                guesses=''.join(guesses_list) # Перевод массива в строку
        if guesses.find('*') ==-1: # Проверка на всё слово
            print(guesses)
            print ('Победа!')
            break
        if word.find(letter) == -1: # Проверка на ошибочную попытку
            attempt=attempt+1
if attempt==max_attempts:
    print ('Проигрыш. Слово:', word)