"""
5
Напишите программу, которая циклично запрашивает у пользователя номера
символов по таблице Unicode и выводит соответствующие им символы.
Завершает работу при вводе нуля.

Напишите программу, которая измеряет длину введенной строки. Если
строка длиннее десяти символов, то выносится предупреждение. Если
короче, то к строке добавляется столько символов *, чтобы ее длина
составляла десять символов, после чего новая строка должна выводиться
на экран.

Напишите программу, которая запрашивает у пользователя шесть
вещественных чисел. На экран выводит минимальное и максимальное из них,
округленные до двух знаков после запятой. Выполните задание без
использования встроенных функций min() и max().

"""
# a
number = int(input("Введите порядковый номер символа Unicode: "))

while number != 0:
    # print(chr(number))
    print("Ваш Unicode: ", chr(number))
    number = int(input("Введите следующий номер символа Unicode: "))

if number == 0:
    print("Ваш номер 0")


# b
user_str = input("Введите Вашу строку: ")
len_str = 10

if len(user_str) > len_str:
    print("Warning!! Ваша строка привышает 10 символов")

elif len(user_str) < len_str:
    # s = len_str - len(user_str)
    print(user_str + (len_str - len(user_str)) * "*")


# c
from functools import reduce

user_num = []

enter_num = input("Введите шесть вещественных чисел: ").split()
for x in enter_num:
    user_num.append(x)
print("Ваш список: ", user_num)

max_num = reduce(max, user_num)
min_num = reduce(min, user_num)

print(round(float(max_num), 2))
print(round(float(min_num), 2))
