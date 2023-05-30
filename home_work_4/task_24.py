lst = list(map(int, input().split()))
print(max(lst[i - 1] + lst[i] + lst[(i + 1) % len(lst)] for i in range(len(lst))))
