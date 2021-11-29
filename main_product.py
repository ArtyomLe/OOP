from product import Product

products = [
    Product("Болты и гайки", 5, 500),
    Product("Зубные щётки", 20, 100),
    Product("Мясорубки", 750, 300),
    Product("Насадки для пылесоса", 2100, 150),
    Product("Футляры", 1000, 10),
    Product("Учебники по Python", 1100, 50)
    ]

def printHead(s): # Заголовок
    print("=" * 79)
    print(s)
    print("=" * 79)

def printList(): # Содержимое трюма в виде таблицы
    printHead("СТАТИСТИКА:")
    for i in range(len(products)):
        print(f"{(i + 1):3}. {products[i]}") # Возвращаемая строка указана в методе __str__ класса

def sumAll(): # Возвращает общую сумму
    total_cost = 0
    for p in products:
        total_cost += p.getPrice()
    return total_cost

def printTotalCost(): # Строка с общей суммой
    printHead(f"ОБЩАЯ СТОИМОСТЬ: {sumAll()} руб.")

playGame = True
while playGame:
    print("\n")         # Выводим пустую строку
    printList()         # Выводим все товары в виде таблицы
    printTotalCost()    # Выводим общую стоимость всех товаров

    n = int(input("Введите номер товара, с которым желаете работать (0 - выход): "))
    if n == 0:
        playGame = False
    elif n > 0 and n <= len(products):
        products[n - 1].menu()
print("Успешного полёта, капитан!")
