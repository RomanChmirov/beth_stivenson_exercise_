# Импортируем из модуля time функции, необходимые для выполнения программы
from time import asctime

# Вычисляем текущее время
time_is_now = asctime()

# Выводим результат
print(f"Теперешнее время: {time_is_now}.")
