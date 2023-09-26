from exercise_106 import days_in_month


## Функция определяет, является ли дата магической
# @param a — номер дня
# @param b — номер месяца
# @param c — год
# @return True или False
def magic_date(a, b, c):

    result = True if a * b == c else False

    return result


def main():
    MIN_YEAR = 1901
    MAX_YEAR = 2000
    CONST_TO_CUT = 100

    for i in range(MIN_YEAR, MAX_YEAR + 1):
        for j in range(1, 12 + 1):
            day = days_in_month(j, i)
            for l in range(1, day + 1):
                magic = magic_date(l, j, i % CONST_TO_CUT)

                if magic:
                    print("%02i.%02i.%i" % (l, j, i))


main()
