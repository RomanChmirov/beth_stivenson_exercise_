# Запрашиваем год у пользователя
year = int(input("Введите год: "))


# Вычисляем "високосность" года
if year % 400 == 0:
    classification = "високосный"
elif year % 100 == 0:
    classification = "невисокосный"
elif year % 4 == 0:
    classification = "високосный"
else:
    classification = "невисокосный"


# Выводим результат
print(f"Введённый год — {classification}.")
