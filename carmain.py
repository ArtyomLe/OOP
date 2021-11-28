from car import Car

cars = []
cars.append(Car("Polo", 1999, "White", "Hatchback"))
cars.append(Car("Fiesta", 2014, "DeepBlue", "Hatchback"))
cars.append(Car("Sx4", 2018, "Grey", "Hatchback"))

for c in cars:
    print(f"{c.name}, {c.form}, {c.color}, {c.year}, на дорогах уже: {2021 - c.year} года(лет)")