# Задание 3 (вариант 7). Уценка оборудования
stoimost = float(input("Введите первоначальную стоимость оборудования в руб.: "))
proc = float(input("Введите процент уценки за год: "))
predel = float(input("Введите предельную стоимость в руб.: "))
god = 0
while stoimost > predel:
    stoimost = stoimost - stoimost * proc / 100
    god = god + 1
print("Через", god, "лет стоимость оборудования станет меньше", predel, "руб.")
print("Она составит", round(stoimost, 2), "руб.")
