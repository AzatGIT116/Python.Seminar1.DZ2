# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите число ')
count = 0
for i in n:
    if i != '.' and i != ',':        
        count += int(i)
print(count)


# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите N = '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, sep=' ', end=' ')
  


# 3.Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.

n = int(input('Введите число '))
def sequence(n):
    return [round((1 + 1 / n) ** n, 2) for n in range(1, n + 1)]
print(sequence(n))
print(round(sum(sequence(n))))


# 4.Реализуйте алгоритм перемешивания списка.

import random 
list = [100, 200, 300, 400]
random.shuffle(list) 
print(list)