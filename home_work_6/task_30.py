a1, d, n = map(int, input().split())
print(*(a1 + d * i for i in range(n)))