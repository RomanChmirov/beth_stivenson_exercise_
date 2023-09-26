from exercise_91 import ordinalDate


## Функция переводит порядковую дату в григорианский календарь
# @param a — порядковый номер дня
# @param с — год
# @return дата в григорианском календаре
def gregorianDate(a, c):
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

    # Вычисляем номер месяца
    if classification == "невисокосный":

        if 0 < a <= 31:
            m = 1
        elif 31 < a <= 59:
            m = 2
        elif 59 < a <= 90:
            m = 3
        elif 90 < a <= 120:
            m = 4
        elif 120 < a <= 151:
            m = 5
        elif 151 < a <= 181:
            m = 6
        elif 181 < a <= 212:
            m = 7
        elif 212 < a <= 243:
            m = 8
        elif 243 < a <= 273:
            m = 9
        elif 273 < a <= 304:
            m = 10
        elif 304 < a <= 334:
            m = 11
        elif 334 < a <= 365:
            m = 12

    elif classification == "високосный":

        if 0 < a <= 31:
            m = 1
        elif 31 < a <= 60:
            m = 2
        elif 60 < a <= 91:
            m = 3
        elif 91 < a <= 121:
            m = 4
        elif 121 < a <= 152:
            m = 5
        elif 152 < a <= 182:
            m = 6
        elif 182 < a <= 213:
            m = 7
        elif 213 < a <= 244:
            m = 8
        elif 244 < a <= 274:
            m = 9
        elif 274 < a <= 305:
            m = 10
        elif 305 < a <= 335:
            m = 11
        elif 335 < a <= 366:
            m = 12

    # Вычисляем номер дня
    for i in range(0, m - 1):

        if i == 4 or i == 6 or i == 9 or i == 11:
            n += 30
        elif i == 2:
            n += 29 if classification == "високосный" else 28
        else:
            n += 31

    d = a - n

    return "%.2i.%.2i" % (d, m)


# Запрашиваем у пользователя данные
day = int(input("Введите день(цифрами): "))
month = int(input("Введите месяц(цифрами): "))
year = int(input("Введите год(цифрами): "))
number_of_days = int(input("Введите кол-во дней для расчёта следующей даты: "))

day_number = ordinalDate(day, month, year)

all_days = day_number + number_of_days


if all_days > 365:
    year += 1
    new_day_number = all_days - 365
else:
    new_day_number = all_days


# Заносим новую дату в переменную
full_date = f"{gregorianDate(new_day_number, year)}.{year}"

# Выводим результат
print(full_date)
