lst = list(map(int, input().split()))
print(sum(0 < i < len(lst) - 1 and lst[i - 1] < lst[i] and lst[i + 1] < lst[i] for i in range(len(lst))))