
from codeint import CodeInt
from random import randint

n = randint(5, 15)
cInt = []
for i in range(n):
    cInt.append(CodeInt(randint(0, n * 5)))

for c in cInt:
    print(c.digit)    # Выводим текстовое предсталение списка через в закодированном виде