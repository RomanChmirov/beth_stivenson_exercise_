# Цена за одну буханку хлеба в долларах
PRICE_ONE_BREAD = 3.49
# Скидка на вчерашний хлеб в процентах
DISCOUNT_BREAD = 0.6

# Запрашиваем у пользователя кол-во приобретённых вчерашних буханок хлеба
quantity_bread = int(input("Сколько буханок вчерашнего хлеба вы хотите приобрести? "))

# Вычисляем цену на хлеб без скидки, скидку и конечную цену
price_without_discount = PRICE_ONE_BREAD * quantity_bread
price_with_discount = PRICE_ONE_BREAD * (1 - DISCOUNT_BREAD) * quantity_bread
all_price = price_without_discount - price_with_discount

# Выводим обычную цену за буханку хлеба
print("Обычная цена хлеб: %.2f;" % price_without_discount)
print("Скидка на хлеб: %.2f;" % price_with_discount)
print("Конечная цена за хлеб: %.2f." % all_price)
