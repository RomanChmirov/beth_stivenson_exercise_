def typical_list(l: list) -> str:
    new_l = []
    result = ''

    if len(l) == 1:
        new_l.append(l[0])
    elif len(l) == 2:
        new_l.append(str(l[0]))
        new_l.append(' и ')
        new_l.append(str(l[1]))
    else:
        for i in l[0: len(l) - 2]:
            new_l.append(str(i))
            new_l.append(', ')
        new_l.append(str(l[len(l) - 2]))
        new_l.append(' и ')
        new_l.append(str(l[len(l) - 1]))

    for j in new_l:
        result += j

    return result


def main():
    lst = []

    item = input("Введите элемент списка: ")
    while item:
        lst.append(item)
        item = input("Введите элемент списка(для прекращения ввода Enter): ")

    print(f"Отформатированная строка: {typical_list(lst)}")


main()
