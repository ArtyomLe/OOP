
from codeint import CodeInt

print("Десятичная форма числа")
a = CodeInt(0)
b = CodeInt(1)
print(f"{a} {b}", end=" ")
for i in range(20):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

print("\nВнутренняя форма числа")
a = CodeInt(0)
b = CodeInt(1)
print(f"{a.digit} {b.digit}", end=" ")
for i in range(20):
    c = a + b
    print(c.digit, end=" ")
    a = b
    b = c
