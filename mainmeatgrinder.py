from meatGrinder import MeatGrinder

grid = []
grid.append(MeatGrinder("Brass", 80, 3*2 + 4*2 + 5, "polygon"))
grid.append(MeatGrinder("Steel", 86, 9, "X"))
grid.append(MeatGrinder("Plastic", 60, 7, "+"))
grid.append(MeatGrinder("Silver", 82, 9, "*"))

for g in grid:
    print(f"{g.material}, {g.size}, {g.holes}, {g.figure}")