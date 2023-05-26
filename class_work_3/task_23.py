lst = list(map(int, input().split()))
print(sum(lst[i] > lst[i - 1] for i in range(1, len(lst))))