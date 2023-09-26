print("Введите дату.")
year = int(input("Введите год(цифрами): "))  # год
month = int(input("Введите месяц(цифрами): "))  # месяц
day = int(input("Введите день(цифрами): "))  # день

# Увеличиваем год, если нужно
if month == 12 and day == 31:
    month = 1
    day = 1
    year += 1

# Увеличиваем месяц, если нужно
elif ((month == 4 or month == 6 or month == 9 or month == 11) and day == 30) or \
        ((month == 1 or month == 3 or month == 5 or
          month == 7 or month == 8 or month == 10) and day == 31):
    month += 1
    day = 1

elif month == 2:

    if year % 400 == 0:
        classification = "високосный"
    elif year % 100 == 0:
        classification = "невисокосный"
    elif year % 4 == 0:
        classification = "високосный"
    else:
        classification = "невисокосный"

    if (classification == "високосный" and day == 29) or (classification == "невисокосный" and day == 28):
        month += 1
        day = 1
    else:
        day += 1

# Увеличиваем день, если нужно
else:
    day += 1


# Выводим результат
print("Дата следующего дня: %.2i.%.2i.%.2i" % (day, month, year))
