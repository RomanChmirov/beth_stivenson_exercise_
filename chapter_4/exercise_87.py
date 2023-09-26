# Задаём константы
PRICE_FOR_THE_FIRST_ITEM = 10.95  # цена за первый товар
PRICE_OF_THE_FOLLOWING_PRODUCT = 2.95  # цена за следующие товары

# Запрашиваем данные у пользователя
number_of_goods = int(input("Введите кол-во товаров в заказе: "))


## Функция вычисляет стоимость доставки
# @param a — кол-во товаров в заказе
# @return стоимость доставки товаров
def calculate_the_cost(a):
    return PRICE_FOR_THE_FIRST_ITEM + (a - 1) * PRICE_OF_THE_FOLLOWING_PRODUCT


# Находим стоимость доставки
shipping_cost = calculate_the_cost(number_of_goods)

# Выводим результат
print(f"Стоимость доставки {number_of_goods} товаров: {shipping_cost}.")
