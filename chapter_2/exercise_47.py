# Запрашиваем у пользователя название месяца и номер дня
month = input("Введите название месяца(с маленькой буквы): ")
day = int(input("Введите номер дня(цифрами): "))

# Создаём переменную для названия сезона года
season = ''


# Вычисляем сезон года
if (0 < day <= 31) and \
        (month == "декабрь" or month == "январь" or month == "февраль"
         or month == "март" or month == "апрель" or month == "май"
         or month == "июнь" or month == "июль" or month == "август"
         or month == "сентябрь" or month == "октябрь" or month == "ноябрь"):

    if (month == "март" and day >= 20) or (month == "апрель") \
            or (month == "май") or (month == "июнь" and day < 21):
        season = "весна"

    elif (month == "июнь" and day >= 21) or (month == "июль") or (month == "август") \
            or (month == "сентябрь" and day < 22):
        season = "лето"

    elif (month == "сентябрь" and day >= 22) or (month == "октябрь") or (month == "ноябрь") \
            or (month == "декабрь" and day < 21):
        season = "осень"

    elif (month == "декабрь" and day >= 21) or (month == "январь") \
            or (month == "февраль" and 0 < day <= 29) or (month == "март" and day < 20):
        season = "зима"

    else:
        season = "не определена, т. к. вы указали некорректные данные"

else:
    season = "не определена, т. к. вы указали некорректные данные"


# Выводим результат
print(f"Пора года — {season}.")
