# Кол-во часов в дне, минут в часу, секунд в минуте
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

# Запрашиваем кол-во дней, часов, минут, секунд соответственно во временном промежутке
days = int(input("Введите ко-во дней во временном промежутке:"))
hours = int(input("Введите ко-во часов во временном промежутке:"))
minutes = int(input("Введите ко-во минут во временном промежутке:"))
seconds = int(input("Введите ко-во секунд во временном промежутке:"))

# Считаем кол-во секунд во временном промежутке
all_seconds = ((days * HOURS_IN_DAY + hours) * MINUTES_IN_HOUR + minutes) * SECONDS_IN_MINUTE + seconds

# Выводим результат
print(f"Время в секундах: {all_seconds}.")
