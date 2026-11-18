# Задание 1 (вариант 7). Сумма квадратов чисел от A до B
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
summa = 0
for i in range(a, b + 1):
    summa = summa + i * i
print("Сумма квадратов чисел от", a, "до", b, "равна", summa)
