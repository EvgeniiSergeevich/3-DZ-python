# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_num = int(input('Введите десятичное число: '))
bin_num = bin(dec_num)[2::]
print(bin_num)