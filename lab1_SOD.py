print('Первое');
a=2963+8877;
print('Ответ',a);

print('Второе');
b=7321-3450;
print('Ответ',b);


print('Третье');
с=456*745;
print('Ответ',с);

print('Четвертое');
d=4592/42;
print('Ответ',d);


print('Пятое');
print('Ответ', pow(29, 7))

print('Шестое');
import math
print(math.sqrt(666))




print('Задание 2')
import sympy
print(sympy.factorint(123456, visual=True))
print(sympy.factorint(565665, visual=True))


from sympy import ceiling, floor

print('Задание 3')
rounded_up = ceiling(2.462)
print("Округлить до большего целого:", rounded_up)
rounded_down = floor(2.462)
print("Округлить до меньшего целого:", rounded_down)

print('Задание 4')
from sympy import Abs
numbers = [-1.8, 66]
absolute_values = [Abs(num) for num in numbers]
print("Модуль -1.8:", absolute_values[0])
print("Модуль 66:", absolute_values[1])

print('Задание 5')
from sympy import gcd, lcm
a = 392
b = 35

remainder = a % b
print("Остаток от деления 392 на 35:", remainder)
greatest_common_divisor = gcd(a, b)
print("Наибольший общий делитель (НОД) 392 и 35:", greatest_common_divisor)
least_common_multiple = lcm(a, b)
print("Наименьшее общее кратное (НОК) 392 и 35:", least_common_multiple)
  
print('Задание 6')
from sympy import sin, pi, atan, oo, exp, ln, factorial

sin_pi_6 = sin(pi/6)
print("sin(π/6):", sin_pi_6)
arctan_inf = atan(oo)
print("arctg(∞):", arctan_inf)
e_n = exp(1)
print("e:", e_n)
ln_6 = ln(6)
print("ln(6):", ln_6)
factorial_6 = factorial(6)
print("6!:", factorial_6)
 

print('Задание 7')
z1 = 1 + 5j
import cmath

print("Вещественная часть:", z1.real)
print("Мнимая часть:", z1.imag)
print("Модуль:", abs(z1))
print("Аргумент:", cmath.phase(z1))

import cmath

z2 = (5j) / (9 + 1j)

print("Вещественная часть:", z2.real)
print("Мнимая часть:", z2.imag)
print("Модуль:", abs(z2))
print("Аргумент:", cmath.phase(z2))
