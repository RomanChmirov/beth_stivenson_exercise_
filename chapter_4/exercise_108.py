TEASPOONS_IN_TABLESPOON = 3
TABLESPOONS_IN_CUP = 16


## Функция рассчитывает минимальное кол-во действий и предметов для измерения данного объёма
# @param t — общий объём (в минимальной мере измерения)
# @return минимальное кол-во действий и предметов
def min_measurements(t):

    new_cups = t // (TABLESPOONS_IN_CUP * TEASPOONS_IN_TABLESPOON)
    new_tablespoons = t % (TABLESPOONS_IN_CUP * TEASPOONS_IN_TABLESPOON) // 3
    new_teaspoons = t % (TABLESPOONS_IN_CUP * TEASPOONS_IN_TABLESPOON) % 3

    return new_cups, new_tablespoons, new_teaspoons


def main():
    cups = 0
    tablespoons = 0
    teaspoons = 0

    x = input("Хотите ввести какую-либо меру измерения ингредиентов? ")
    while x == 'Да' or x == 'да':
        container = input("Введите измерительную ёмкость(cup, tablespoon или teaspoon): ")


        if container == 'cup' or container == 'tablespoon' or container == 'teaspoon':
            quantity_containers = int(input("Введите кол-во измерительных ёмкостей: "))

            if container == 'cup':
                cups += quantity_containers
            elif container == 'tablespoon':
                tablespoons += quantity_containers
            elif container == 'teaspoon':
                teaspoons += quantity_containers

        else:
            print("Такой меры измерения в нашей программе не предусмотрено!")

        x = input("Хотите ввести  ещё одну меру измерения ингредиентов? ")

    total = (cups * TABLESPOONS_IN_CUP + tablespoons) * TEASPOONS_IN_TABLESPOON + teaspoons
    (final_count_cups, final_count_tablespoons, final_count_teaspoons) = min_measurements(total)

    print(f"{final_count_cups} cup(s), {final_count_tablespoons} tablespoon(s), {final_count_teaspoons} teaspoon(s)")


main()
