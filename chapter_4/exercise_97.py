## Функция определяет приоритет математического оператора
# @param s — оператор
# @return 1, 2, 3 или -1(в зависимости от приоритета и правильности ввода оператора)
def precedence(s):

    if s == '+' or s == '-':
        prior = 1
    elif s == '/' or s == '*':
        prior = 2
    elif s == '^':
        prior = 3
    else:
        prior = -1

    return prior


def main():
    operator = input("Введите оператор: ")
    priority = precedence(operator)

    if priority == -1:
        result = "Ошибка! Вы ввели не оператор."
    else:
        result = f"Приоритет оператора — {priority}."

    print(result)


if __name__ == "__main__":
    main()
