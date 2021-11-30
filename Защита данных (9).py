cString = "НУПРИВЕТ"

n = 97
base = len(cString)
res = ""

if n == 0:
    res = cString[0]
else:
    while n > 0:
        res = cString[n % base] + res
        n //= base

print(res)