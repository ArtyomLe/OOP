n = 79
base = 8
res = " "

while n > 0:
    res = str(n % base) + res           # (79 % 8 = 7)    (9 % 8 = 1)    (1 % 8 = 1)   res = "1 + 1 + 7" = 117
    n //= base                          # (79 // 8 = 9)   (9 // 8 = 1)   (1 // 8 = 0)

print(res)
