from exercise_104 import *


## Функция преобразовывает строку из любой системы счисление в число в десятичной системе счисления
# @param line — строка в любой системе счисления
# @param x — основание системы счисления
# @return число в десятичной системе счисления
def x2int(line, x):

    if not 2 <= x <= 16:
        return "Ошибка! Вы ввели систему, основание которой не выходит в диапазон 2 — 16."

    result = 0
    index_number = len(line) - 1

    for i in line:

        i = hex2int(i)
        result += int(i) * (x ** index_number)
        index_number -= 1

    return result


## Функция преобразовывает число из десятичной системы счисление в строку в любой системе счисления
# @param integer — число в десятичной системе счисления
# @param x — основание системы счисления
# @return строка в любой системе счисления
def int2x(integer, x):

    if not 2 <= x <= 16:
        return "Ошибка! Вы ввели систему, основание которой не выходит в диапазон 2 — 16."

    result = ''

    while integer > 0:
        remainder = integer % x
        remainder = int2hex(remainder)

        result += str(remainder)

        integer = integer // x

    result = result[:: -1]

    return result


def main():
    original_number_system = int(input("Введите основание исходной системы счисления: "))
    finite_number_system = int(input("Введите основание конечной системы счисления: "))
    original_number = input("Введите число в исходной системе счисления: ")

    finite_number = int2x(x2int(original_number, original_number_system), finite_number_system)

    print(finite_number)


main()
