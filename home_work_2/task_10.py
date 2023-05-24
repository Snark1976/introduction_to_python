n, summa = int(input()), 0
for _ in range(n):
    summa += int(input())
print(min(summa, n - summa))
