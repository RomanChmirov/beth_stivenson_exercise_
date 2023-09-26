from exercise_98 import isPrime


## Функция возвращает простое число большее заданного
# @param n — целое число
# @return простое число
def nextPrime(n):
    j = n + 1

    while True:

        if isPrime(j):
            return j
        else:
            j += 1


def main():
    number = int(input("Введите целое число: "))
    result = nextPrime(number)
    print(result)


main()
