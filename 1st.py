# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

l = list(map(int, input("Введите числа через пробел: ").split()))
summa = sum(l[1::2])
print(f"Сумма нечётных элементов равна {summa}")