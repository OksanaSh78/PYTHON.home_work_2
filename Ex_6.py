# Задача 2
# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


number = int(input('Для числа:  '))
my_list = []
for n in range(1, number+1):
    my_list.append(round((1+1/n)**n, 2))
print(my_list)
#sum = 0   
# sum([my_list])
# print(sum)
print(f'Сумма: {round(sum(my_list), 3)}')
