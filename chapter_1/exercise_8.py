# Цены на сувенир и безделушку соответственно
WEIGHT_SUV = 75
WEIGHT_BEZ = 115

# Запрашиваем у пользователя кол-во сувениров и безделушек
quantity_suv = int(input("Сколько у вас сувениров? "))
quantity_bez = int(input("Сколько у вас безделушек? "))

# Считаем цену за покупку
all_weight = WEIGHT_SUV * quantity_suv + WEIGHT_BEZ * quantity_bez

# Выводим результат
print(f"Общий вес посылки: {all_weight}(г).")
