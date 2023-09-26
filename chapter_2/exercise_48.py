# Запрашиваем у пользователя название месяца и номер дня
month = input("Введите название месяца(с маленькой буквы): ")
day = int(input("Введите номер дня(цифрами): "))

# Создаём переменную для названия знака зодиака
sign = ''


# Вычисляем знак зодиака
if (0 < day <= 31) and \
        (month == "декабрь" or month == "январь" or month == "февраль"
         or month == "март" or month == "апрель" or month == "май"
         or month == "июнь" or month == "июль" or month == "август"
         or month == "сентябрь" or month == "октябрь" or month == "ноябрь"):

    if month == "декабрь":

        if day >= 22:
            sign = "козерог"
        else:
            sign = "стрелец"

    elif month == "январь":

        if day >= 20:
            sign = "водолей"
        else:
            sign = "козерог"

    elif month == "февраль" and day != 30 and day != 31:

        if 19 <= day <= 29:
            sign = "рыбы"
        else:
            sign = "водолей"

    elif month == "март":

        if day >= 21:
            sign = "овен"
        else:
            sign = "рыбы"


    elif month == "апрель":

        if day >= 20:
            sign = "телец"
        else:
            sign = "овен"

    elif month == "май":

        if day >= 21:
            sign = "близнецы"
        else:
            sign = "телец"

    elif month == "июнь":

        if day >= 21:
            sign = "рак"
        else:
            sign = "близнецы"


    elif month == "июль":

        if day >= 23:
            sign = "лев"
        else:
            sign = "рак"

    elif month == "август":

        if day >= 23:
            sign = "дева"
        else:
            sign = "лев"

    elif month == "сентябрь":

        if day >= 23:
            sign = "весы"
        else:
            sign = "дева"

    elif month == "октябрь":

        if day >= 23:
            sign = "скорпион"
        else:
            sign = "весы"

    elif month == "ноябрь":

        if day >= 22:
            sign = "стрелец"
        else:
            sign = "скорпион"

    else:
        sign = "не определен, т. к. вы указали некорректные данные"

else:
    sign = "не определен, т. к. вы указали некорректные данные"


# Выводим результат
print(f"Знак зодиака — {sign}.")
