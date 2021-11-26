# НОД => Наибольший общий делитель двух чисел
a = int(input("Введите А: "))
b = int(input("Введите В: "))

while (a != 0) and (b != 0):
    if (a > b):
        a %= b
    else:
        b %= a

print(f"НОД = {a+b}")
