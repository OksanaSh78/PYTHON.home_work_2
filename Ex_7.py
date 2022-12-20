# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int


import random
list = [0,1,2,3,4,5,6,7,8,9]
print(list)
for a in range(len(list)-1, 0, -1):
    b = random.randint(0, a + 1) 
    list[a], list[b] = list[b], list[a] 
print(list)    
