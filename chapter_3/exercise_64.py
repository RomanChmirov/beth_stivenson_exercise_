# Вводим константы
SALE = 0.6  # скидка на товары
# цены на товары в $
PRISE_1 = 4.95


# Выводим цены
for i in range(5):
    # Считаем цену, скидку, цену с учётом скидки
    prise = PRISE_1 + 5 * i
    sale_cash = prise * SALE
    new_prise = prise - sale_cash

    # Выводим результат
    print("Исходная цена на товар: %.2f; Скидка на товар: %.2f; Цена со скидкой: %.2f." % (prise, sale_cash, new_prise))
