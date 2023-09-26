from exercise_100 import generates_password
from exercise_102 import password_strength


## Функция генерирует надёжный пароль
# @return надёжный пароль
def strong_password():
    # Задаём переменную для счётчика попыток и делаем её глобальной
    global i
    i = 0
    strength = False

    # генерируем пароль до то момента, пока он не будет надёжным
    while not strength:
        i += 1
        result = generates_password()
        strength = password_strength(result)

    return result


def main():
    password = strong_password()
    print(f"Надёжный пароль: {password}. Кол-во попыток для создания надёжного пароля: {i}.")


main()
