# Задание 2 (вариант 7). Вычисление cos(x) в виде произведения
# cos(x) = (1 - 4*x^2/pi^2) * (1 - 4*x^2/(9*pi^2)) * ...
# Сомножители перемножаются, пока погрешность не станет меньше e
import math
x = float(input("Введите x: "))
e = float(input("Введите точность e: "))
proizv = 1.0
n = 0
while abs(proizv - math.cos(x)) >= e:
    n = n + 1
    somnozh = 1 - 4 * x * x / ((2 * n - 1) ** 2 * math.pi ** 2)
    proizv = proizv * somnozh
print("Произведение:", proizv)
print("cos(x):", math.cos(x))
print("Число сомножителей:", n)
