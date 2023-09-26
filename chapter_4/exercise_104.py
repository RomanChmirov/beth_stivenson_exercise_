## Функция преобразовывает строку из шестнадцатеричной системы счисление в число в десятичной
# @param hex_sym — строка в шестнадцатеричной системе счисления
# @return число в десятичной системе счисления
def hex2int(hex_sym):

    # Если строка является числом от 0 до 9, то оставляем её без изменений
    if '0' <= hex_sym <= '9':
        result = int(hex_sym)
    # Преобразовываем буквы в числа
    elif hex_sym == 'A' or hex_sym == 'a':
        result = 10
    elif hex_sym == 'B' or hex_sym == 'b':
        result = 11
    elif hex_sym == 'C' or hex_sym == 'c':
        result = 12
    elif hex_sym == 'D' or hex_sym == 'd':
        result = 13
    elif hex_sym == 'E' or hex_sym == 'e':
        result = 14
    elif hex_sym == 'F' or hex_sym == 'f':
        result = 15
    else:
        result = "Ошибка! Вы введи число не входящее в диапазон."

    return result


## Функция преобразовывает число из десятичной системы счисление в строку в шестнадцатеричной системе счисления
# @param int_sym — число в десятичной системе счисления
# @return строка в шестнадцатеричной системе счисления
def int2hex(int_sym):
    int_sym = int(int_sym)

    # Если число находится в диапазоне от 0 до 9, то оставляем его без изменений
    if 0 <= int_sym <= 9:
        result = str(int_sym)
    # Преобразовываем числа в буквы
    elif int_sym == 10:
        result = 'A'
    elif int_sym == 11:
        result = 'B'
    elif int_sym == 12:
        result = 'C'
    elif int_sym == 13:
        result = 'D'
    elif int_sym == 14:
        result = 'E'
    elif int_sym == 15:
        result = 'F'
    else:
        result = "Ошибка! Вы введи число не входящее в диапазон."

    return result
