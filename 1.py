# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите 
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0

from random import randint 

n = int(input('Введите число монет: '))
print()

rawOfCoins = []  

for i in range(n):
    coin = randint(0, 1) 
    rawOfCoins.insert(i, coin)

zeroNumber = rawOfCoins.count(0) 
oneNumber = rawOfCoins.count(1) 

print(f'Для полученных {n} монет выпали значения: {rawOfCoins}.'
    f'\n В том числе значения \"0\" для {zeroNumber} монет, '
    f'значения \"1\" для {oneNumber} монет.') 

if (zeroNumber >= oneNumber): print(f'Необходимо перевернуть {oneNumber} монет.')
else: print(f'Необходимо перевернуть {zeroNumber} монет.')