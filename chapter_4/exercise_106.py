## Функция определяет кол-во дней в месяце
# @param num — номер месяца
# @param year — год
# @return кол-во дней в месяце
def days_in_month(num, year):

    # Вычисляем "високосность" года
    if year % 400 == 0:
        classification = "високосный"
    elif year % 100 == 0:
        classification = "невисокосный"
    elif year % 4 == 0:
        classification = "високосный"
    else:
        classification = "невисокосный"

    # Вычисляем кол-во дней в месяце
    if num == 4 or num == 6 or num == 9 or num == 11:
        result = 30
    elif num == 2:
        result = 28 if classification == "невисокосный" else 29
    else:
        result = 31

    return result


def main():
    month_number = int(input("Введите номер месяца: "))
    year = int(input("Введите номер года: "))

    days = days_in_month(month_number, year)

    print(f"Количество дней в месяце под номером {month_number} равняется {days}.")


if __name__ == "__main__":
    main()
