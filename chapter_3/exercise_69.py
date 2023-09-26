# Задаём константы
NEWBORNS_TICKET = 0
CHILDREN_TICKET = 14
PENSIONERS_TICKET = 18
ADULT_TICKET = 23

# Запрашиваем возраст посетителя
age = input("Введите возраст посетителя: ")

# Задаём нулевое значение для общей цены
all_price = 0


while age:
    # Преобразуем возраст в целое число
    age = int(age)

    # Вычисляем цену за билет
    if age <= 2:
        ticket_price = NEWBORNS_TICKET

    elif 2 < age <= 12:
        ticket_price = CHILDREN_TICKET

    elif 12 < age <= 65:
        ticket_price = ADULT_TICKET

    elif 65 < age:
        ticket_price = PENSIONERS_TICKET

    all_price += ticket_price

    age = input("Введите возраст следующего посетителя(для остановки подсчёта нажмите Enter): ")


# Выводим результат
print("Общая цена за всех посетителей: %.2f." % all_price)
