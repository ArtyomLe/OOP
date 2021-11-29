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