from exercise_115 import own_divisors


## Функция определяет, является ли число совершенным
# @param n — число
# @return True или False
def perfect_number(n):
    result = True if sum(own_divisors(n)) == n else False

    return result


def main():
    for i in range(1, 10001):
        if perfect_number(i):
            print(i)


main()
