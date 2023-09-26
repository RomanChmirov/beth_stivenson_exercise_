# Услуги входящие в тарифный план
TARIFF_MINUTES = 50
TARIFF_MESSAGES = 50
# и стоимость тарифа без дополнительных услуг
TARIFF = 15

# Стоимости дополнительных услуг
ADDITIONAL_MINUTE_1 = 0.25  # Одна дополнительная минута разговора
ADDITIONAL_MESSAGE_1 = 0.15  # Одно дополнительное сообщение
TAX_911 = 0.44  # Налог на поддержку кол-центров 911
TOTAL_TAX = 0.05  # Налог в процентах на общую сумму

# Запрашиваем у пользователя ко-во минут и смс-сообщений
minutes = int(input("Введите количество израсходованных минут разговора за месяц(цифрами): "))
messages = int(input("Введите количество отправленных смс-сообщений за месяц(цифрами): "))


# Высчитываем кол-во дополнительных минут и сообщений(или же их отсутствие)
over_minutes = minutes - TARIFF_MINUTES if minutes > 50 else 0
over_messages = messages - TARIFF_MESSAGES if messages > 50 else 0


# Считаем сумму для оплаты за дополнительные минуты и сообщения
over_minutes_cash = over_minutes * ADDITIONAL_MINUTE_1
over_messages_cash = over_messages * ADDITIONAL_MESSAGE_1
# и сумму налога
total_tax_cash = (TARIFF_MINUTES + TARIFF_MESSAGES + over_minutes_cash + over_messages_cash + TAX_911) * TOTAL_TAX

# Считаем общую сумму с учётом налога
all_cash = TARIFF + over_minutes_cash + over_messages_cash + TAX_911 + total_tax_cash

# Выводим результат
print("Базовая сумма тарификации: %.2f;" % TARIFF)


if over_minutes:
    print("Сумма за дополнительные минуты: %.2f;" % over_minutes_cash)


if over_messages:
    print("Сумма за дополнительные сообщения: %.2f;" % over_messages_cash)


print("Сумма отчислений ко-центрам 911: %.2f;" % TAX_911)
print("Налог на общую сумму: %.2f;" % total_tax_cash)
print("Общая сумма для оплаты за месяц: %.2f." % all_cash)
