# Кол-во секунд в дне, в часу, в минуте
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

# Запрашиваем кол-во секунд у пользователя
all_seconds = int(input("Введите кол-во секунд во временном промежутке: "))

# Считаем кол-во дней
days = all_seconds // SECONDS_IN_DAY

# Считаем кол-во часов
all_seconds = all_seconds % SECONDS_IN_DAY
hours = all_seconds // SECONDS_IN_HOUR

# Считаем кол-во минут
all_seconds = all_seconds % SECONDS_IN_HOUR
minutes = all_seconds // SECONDS_IN_MINUTE

# Считаем кол-во секунд
seconds = all_seconds % SECONDS_IN_MINUTE

# Выводим результат
print(f"%i(дн.) : %02i(ч.) : %02i(мин.) : %02i(сек.)" % (days, hours, minutes, seconds))
