if __name__ == "__main__":
    # Запрашиваем у пользователя данные
    day = int(input("Введите день(цифрами): "))
    month = int(input("Введите месяц(цифрами): "))
    year = int(input("Введите год(цифрами): "))


## Функция считает порядковый номер в григорианском календаре
# @param a — номер дня
# @param b — номер месяца
# @param c — номер года
# @return порядковый номер дня в григорианском календаре
def ordinalDate(a, b, c):
    # Задаём нулевое значение номеру дня
    n = 0

    # Вычисляем "високосность" года
    if c % 400 == 0:
        classification = "високосный"
    elif c % 100 == 0:
        classification = "невисокосный"
    elif c % 4 == 0:
        classification = "високосный"
    else:
        classification = "невисокосный"

    # Увеличиваем порядковый номер дня на кол-во дней в месяце
    for i in range(1, b):

        if i == 4 or i == 6 or i == 9 or i == 11:
            n += 30
        elif i == 2:
            n += 29 if classification == "високосный" else 28
        else:
            n += 31

    # Увеличиваем порядковый номер дня на кол-во дней в последнем месяце
    n += a

    return n


if __name__ == "__main__":
    # Находим порядковый номер дня в григорианском календаре
    serial_number_of_the_day = ordinalDate(day, month, year)

    # Выводим результат
    print(f"Порядковый номер дня в {year} году: {serial_number_of_the_day}")
