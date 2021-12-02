from multipliers import Multipliers

digit = Multipliers(199)

print(f"Сумма множителей: {digit.getSumMul()}")
print(f"Число {digit.dgt}, множители: {str(digit)}")

# Если минимальный после единицы множитель
# равен самому числу, то исходное число простое
if (digit.getMinMul() == digit.dgt):
    print("Число простое.")