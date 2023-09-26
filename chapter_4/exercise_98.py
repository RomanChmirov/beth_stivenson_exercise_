## Функция определяет, является ли число простым
# @param num — число
# @return True или False
def isPrime(num):

    if num > 1:
        j = 0

        for i in range(2, num):
            if num % i == 0:
                j += 1

        res = True if j == 0 else False

    else:
        res = False

    return res


def main():
    number = int(input("Введите целое число: "))
    is_prime_number = isPrime(number)

    if is_prime_number:
        result = "Это простое число."
    else:
        result = "Это непростое число."

    print(result)


if __name__ == "__main__":
    main()
