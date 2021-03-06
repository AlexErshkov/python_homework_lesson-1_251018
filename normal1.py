﻿
__author__ = 'Ершков Александр Вячеславович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
a = 3455654609087978
y = 0
while a > 0:
    if a % 10 > y:
        y = a % 10
    a //= 10
print(y)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
b = a + b
a = b - a
b = b - a
print(a)
print(b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print('вычесляем Ax2 + Bx + c = 0')
a = int(input("введи А: "))
b = int(input("введи В: "))
c = int(input("введи C: "))
d = b**2-4*a*c

if d == 0:
    x1=-b/2*a
    x2=x1
elif d>0:
     x1 = (-b + math.sqrt(d))/2*a
     x2 = (-b - math.sqrt(d))/2*a
else:
    x1 = (-b + math.sqrt(math.fabs(d))) / 2 * a
    x2 = (-b - math.sqrt(math.fabs(d))) / 2 * a
print(x1)
print(x2)




