def pow_recursive(x, y):
    return 1 if y < 1 else x * pow_recursive(x, y - 1)

a, b = int(input()), int(input())
print(pow_recursive(a, b))
