from random import randint


## Функция генерирует пароль
# @return пароль
def generates_password():
    pass_word = ''
    len_password = randint(7, 10)

    while len(pass_word) < len_password:
        symbol = chr(randint(33, 126))
        pass_word += symbol

    return pass_word


def main():
    print(generates_password())


if __name__ == "__main__":
    main()
