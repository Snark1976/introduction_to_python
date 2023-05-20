n, m, k = map(int, input().split())
print(('no', 'yes')[k < n * m and ((k % n == 0) or (k % m == 0))])
