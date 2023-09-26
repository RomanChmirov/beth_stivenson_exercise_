# Килопаскалей в футе на квадратный дюйм, миллиметре ртутного столба, атмосфере
KPA_IN_FD = 0.145038
KPA_IN_MRS = 7.50062
KPA_IN_ATM = 0.00986923

# Запрашиваем у пользователя значение давления в килопаскалях
p = float(input("Введите давление(кПа): "))

# Значение давления в футах на квадратный дюйм, миллиметрах ртутного столба, атмосферах
fd = p * KPA_IN_FD
mrs = p * KPA_IN_MRS
atm = p * KPA_IN_ATM

# Выводим результат
print("Давление в атмосферах: %.2f;\n"
      "Давление в миллиметрах ртутного столба: %.2f;\n"
      "Давление в футах на кв. дюйм: %2.f;" % (atm, mrs, fd))
