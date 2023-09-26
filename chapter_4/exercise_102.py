## Функция определяет надёжность пароля
# @param p — пароль, введённый пользователем
# @return True или False
def password_strength(p):

    # Проверяем условие длинны пароля
    condition_1 = True if len(p) >= 8 else False

    # Проверяем условие наличия хотя бы одной буквы в верхнем регистре
    for i in p:

        if 65 <= ord(i) <= 90:
            condition_2 = True
            break

    else:
        condition_2 = False

    # Проверяем условие наличия хотя бы одной буквы в нижнем регистре
    for j in p:

        if 97 <= ord(j) <= 122:
            condition_3 = True
            break

    else:
        condition_3 = False

    # Проверяем условие наличия хотя бы одной цифры
    for l in p:

        if 48 <= ord(l) <= 57:
            condition_4 = True
            break

    else:
        condition_4 = False

    # Проверяем надёжность пароля в совокупности всех условий
    result = True if condition_1 and condition_2 and condition_3 and condition_4 else False

    return result


def main():
    password = input("Введите пароль: ")

    strength = "Пароль надёжный." if password_strength(password) == True else "Пароль не надёжный."

    print(strength)


if __name__ == "__main__":
    main()
