## Функция вычисляет НОД
# @param a — числитель
# @param b — знаменатель
# @return НОД
def gcd(a, b):

    # Вычисляем НОД
    result = min(a, b)

    while a % result or b % result:
        result -= 1

    return result


## Функция сокращает дробь
# @param a — числитель
# @param b — знаменатель
# @return сокращённая дробь
def cut_aFraction(a, b):

    g = gcd(a, b)

    if a == 0:
        return 0, 1


    return int(a / g), int(b / g)


def main():
    numerator = int(input("Введите числитель дроби: "))
    denominator = int(input("Введите знаменатель дроби: "))

    # Вычисляем сокращённую дробь
    (new_numerator, new_denominator) = cut_aFraction(numerator, denominator)


    print("Дробь %i/%i может быть сокращена до %i/%i." % (numerator, denominator, new_numerator, new_denominator))


main()
