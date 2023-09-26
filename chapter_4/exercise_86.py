# Задаём константы
BASE_RATE = 4  # базовый тариф
ADDITIONAL_FEE = 0.25  # дополнительная плата

# Запрашиваем данные у пользователя
travel_distance = float(input("Введите расстояние поездки(м): "))


## Функция считаем цену за поездку
# @param a — расстояние поездки
# @return стоимость поездки
def calculate_the_cost(a):
    return BASE_RATE + ADDITIONAL_FEE * (a / 140)


# Находим стоимость поезди
travel_cost = calculate_the_cost(travel_distance)

# Выводим результат
print(f"Стоимость поездки: {travel_cost}.")
