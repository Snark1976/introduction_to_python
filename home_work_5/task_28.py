def sum_recursive(x, y):
    return x if y < 1 else sum_recursive(x, y - 1) + 1

a, b = int(input()), int(input())
print(sum_recursive(a, b))