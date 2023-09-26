# Запрашиваем у пользователя фразу и кол-во символов для сдвига
phrase = input("Введите фразу: ")
number_of_characters = int(input("Введите кол-во символов для сдвига: "))

alphabet1 = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Задаём переменную для конечного результата
result = ''


# Преобразуем фразу
for i in phrase:

    if i in alphabet1:
        number = ord(i) - ord('a')
        number = (number + number_of_characters) % 26
        symbol = chr(number + ord('a'))

        result += symbol

    elif i in alphabet2:
        number = ord(i) - ord('A')
        number = (number + number_of_characters) % 26
        symbol = chr(number + ord('A'))

        result += symbol

    else:
        result += i


# Выводим результат
print(result)
