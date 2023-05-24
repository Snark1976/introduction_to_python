s, p, x = int(input()), int(input()), 1
while x + p / x != s:
    x += 1
print(x, p // x)