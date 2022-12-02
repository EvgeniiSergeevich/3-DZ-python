# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

num = int(input('Введите целое число: '))


def fib(num):                                             # Получаю значение элемента Фибоначчи
    if num == 0:
        return 0
    elif num in [1, 2]:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

fibonachi = []
for i in range(num + 1):                                    # Получаю последовательность Фибоначчи
    fibonachi.append(fib(i))

def neg_fib(num):                                           # Получаю элемент негофибоначчи
    return ((-1) ** (num + 1)) * fib(num)

nego_fibonachi = []
for i in range(-num - 1, num +1):                           # Получаю последовательность негофибоначчи
    list1 = [neg_fib(i) for i in range(num + 1)][::-1]
    list2 = [fib(i) for i in range(1, num + 1)]
    nego_fibonachi = list1 + list2





print(f'Последовательность Фибоначчи для значения {num}: {fibonachi}')
print(f'Последовательность негоФибоначчи для значения {num}: {nego_fibonachi}')