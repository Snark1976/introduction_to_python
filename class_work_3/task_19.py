lst = list(map(int, input().split()))
k = int(input()) % len(lst) + 1
lst = [lst[i - k] for i in range(len(lst))]
print(lst)
