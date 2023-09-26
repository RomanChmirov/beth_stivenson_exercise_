# Запрашиваем у пользователя строку
string = input("Введите строку: ")

# Задаём переменную для строки без пробелов
string_without_spaces = ''


# Преобразуем строку в строку без пробелов
for j in string:


    if j == ' ':
        b = ''

    else:
        b = j


    string_without_spaces += b


# Вычисляем длину строки без пробелов
len_string_without_spaces = len(string_without_spaces)
# и номер последнего символа
n = len_string_without_spaces - 1

# Задаём переменную для результата "переворачивания строки"
result = ''


# "Пишем" строку наоборот
for i in string_without_spaces:
    a = string_without_spaces[n]

    result += a

    n -= 1


# Выводим результат
if string_without_spaces == result:
    print("Это палиндром.")

else:
    print("Это не палиндром.")
