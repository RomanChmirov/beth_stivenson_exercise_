# Записываем константу для расчёта прибавки к зарплате
const = 2400

# Запрашиваем у пользователя рейтинг сотрудника
rating = float(input("Введите рейтинг сотрудника: "))

# Считаем повышение зарплаты
salary_increase = rating * const


# Вычисляем уровень работы сотрудника
if rating == 0.0:
    rating_value = "низкий"

elif rating == 0.4:
    rating_value = "удовлетворительный"

elif rating >= 0.6:
    rating_value = "высокий"

else:
    rating_value = ''


# Выводим результат
if rating_value == '':
    print("Вы ввели ошибочный рейтинг!!!")

else:
    print(f"Уровень работы сотрудника, согласно введённому рейтингу — {rating_value}."
          f"Прибавка к зарплате в этом случае: {salary_increase}.")
