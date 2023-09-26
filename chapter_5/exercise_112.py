## Функция создаёт копию списка, убирая максимальное и минимальное значения
# @param d — список
# @param n — кол-во экстремальных пар
# @return отформатированная копия списка
def delMinMax_inList(d, n):
    new_d = []
    for i in d:
        new_d.append(i)

    new_d.sort()
    for j in range(n):

        new_d.pop(0)
        new_d.pop()

    return new_d


def main():
    data = []

    # Добавляем введённые элементы в список
    num = int(input("Введите число(для прекращения ввода введите 0): "))
    while num:
        data.append(num)
        num = int(input("Введите число(для прекращения ввода введите 0): "))

    num_pairs = int(input("Введите число экстремальных пар для удаления: "))

    formatted_data = delMinMax_inList(data, num_pairs)

    if len(data) < 4:
        print("Введите более 3 элементов!")
    else:
        print(f"Изначальный список: {data}. Список без выбросов: {formatted_data}")


main()
