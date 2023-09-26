## Функция конвертирует числа в числительные
# @param n — число
# @return числительное
def converting_integers_to_numerals(n):

    if n == 1:
        numeral = "the first"
    elif n == 2:
        numeral = "the second"
    elif n == 3:
        numeral = "the third"
    elif n == 4:
        numeral = "the fourth"
    elif n == 5:
        numeral = "the fifth"
    elif n == 6:
        numeral = "the sixth"
    elif n == 7:
        numeral = "the seventh"
    elif n == 8:
        numeral = "the eighth"
    elif n == 9:
        numeral = "the ninth"
    elif n == 10:
        numeral = "the tenth"
    elif n == 11:
        numeral = "the eleventh"
    elif n == 12:
        numeral = "the twelfth"

    return numeral


if __name__ == "__main__":

    # Выводим результат
    for i in range(1, 13):
        print(f"%3.i | {converting_integers_to_numerals(i)}" % i)
