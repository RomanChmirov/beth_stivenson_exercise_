# Цены на маленькую и большую бутылки соответственно
SA_1 = 0.1
SB_1 = 0.25

# Запрашиваем кол-во бутылок у пользователя
quantity_small_bottle = int(input("Введите кол-во бутылок объёмом до 1 литра(включительно): "))
quantity_big_bottle = int(input("Введите кол-во бутылок объёмом больше 1 литра: "))

# Считаем выручку за сданные бутылки
all_cash = quantity_small_bottle * SA_1 + quantity_big_bottle * SB_1

# Выводим результат
print(f"Сумма, которую вы можете выручить, если сдадите бутылки: ${ all_cash}.")
