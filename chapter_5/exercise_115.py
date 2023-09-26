## Функция ищет собственные делители числа и помещает их в список
# @param n — число
# @return список, состоящий из собственных делителей числа
def own_divisors(n):
    div = []
    n = int(n)

    for i in range(1, n):
        if n % i == 0:
            div.append(i)

    return div


def main():
    number = (input("Введите число: "))
    print(f"Собственные делители числа {number}: ", end='')

    divisors = own_divisors(number)

    for j in range(0, len(divisors) - 1):
        print(divisors[j], end=', ')

    print(f"{divisors[len(divisors) - 1]}.")


if __name__ == "__main__":
    main()
