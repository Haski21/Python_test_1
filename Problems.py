""" 1. Есть список. Найти среднее арифметическое.
    1.1* Какое число нужно добавить, чтобы увеличить среднее арифметическое на 5."""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 111, 612, 219, 12251]
# # Ваш код
# sum = 0
# count = 0
# for _ in a:
#     sum += _
#     count += 1
# print('middle is: ', sum / count)
# '''1.1'''
# print((sum / count + 5) * (count + 1) - sum)

""" 2. Даны списки. Нужно вернуть список, который состоит из элементов,
       общих для этих двух списков."""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Ваш код
# for _ in a:
#     for foo in b:
#         if _ == foo:
#             print(_, end = ' ')
#             break

""" 3. Написать функцию, используя набор букв из модуля string(string.ascii_lowercase),
    которая зашифрует строку. Каждая буква - это две цифры.
    Отчет с 'a' -> 00 и до 'z' -> 25, 26 - это пробел, он не входит в набор букв
    Вход: строка. Выход: цифровая строка.
Пример:
input_line = 'hello python'
out_line = '070411111426152419071413'
"""
# Ваш код
# import string as line
# 
# input_line = 'hello python'
# str = input('Enter string: ') # для общего случая
# 
# if len(str) % 2 != 0 or len(str) == 0: # проверка для общего случая
#     print('Bad string')
# else:
#     for var in range(len(input_line)):
#         foo = input_line[var]
#         counter = 0
#         for _ in line.ascii_lowercase:
#             if foo == ' ':
#                 print('26', end='', sep = '')
#                 counter = 0
#                 break
#             elif  foo == _:
#                 # не понял как взять индекс буквы из line.ascii_lowercase, поэтому сделал счетчик
#                 if counter < 10:
#                     print('0', counter, end = '', sep = '')
#                     counter = 0
#                     break
#                 else:
#                     print(counter, end='', sep = '')
#                     counter = 0
#                     break
#             else:
#                 counter += 1

""" 4. Напишите программу для слияния нескольких словарей в один.
    4.1* Отсортировать полученный словарь по значениям
    4.2* Измените полученный словарь так, чтобы значение стали ключами, а ключи значениями
"""    
# dict_a = {1:15, 2:21}
# dict_b = {3:13, 4:54}
# dict_c = {5:75, 6:68}
# # Ваш код
# dict_a.update(dict_b)
# dict_a.update(dict_c)
# print(dict_a)
# #не совсем разобрался в этом методе
# print(dict(sorted(dict_a.items(), key=lambda item: item[1])))
# 
# dict_e = {value : key for key, value in dict_a.items()}
# dict_e1 = dict((value, key) for key, value in dict_a.items())
# print(dict_e1)

""" 5. Напишите программу, которая из заданного списка выводит только те числа,
    у которых сумма цифр четна и останавливается, если встречает число 237(само число не выводить).
    Порядок элементов не менять!
"""
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
]
# Ваш код

# for foo in numbers:
#     if foo == 237:
#         break
#     else:
#         if not sum((foo // 100, foo // 10 % 10, foo % 10)) % 2:
#             print(foo, end = ' ')
#     

""" 6.Прочитать файл presents.txt. В нем числа - стоимости подарков.
    Вывести на экран список покупок, общую сумму, 2 самые дорогие покупки.
"""
from random import randint, seed
seed(777)
# 
# with open('presents.txt', 'w') as file:
#     for item in range(11):
#         end_flag = ' ' if randint(0, 1) else '\n'
#         print(round(randint(10, 1000) / randint(2, 10), 2), end=end_flag, file=file)

# Ваш код
lst = []
with open('C:\\Users\\Ilya_\\Desktop\\Курсы специалист\\Python уровень 1\\Full_course\\day9-10\\Test\\presents.txt', encoding='utf-8') as file:
    for line in file.readlines():
        lst.extend(list(map(float, line.split())))

print(lst)
print(sum(lst))
max_1 = lst.pop(lst.index(max(lst)))
print(max_1, max(lst))
        