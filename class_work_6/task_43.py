lst = list(map(int, input().split()))
print(sum(lst[i] == lst[j] and i != j for i in range(len(lst)) for j in range(len(lst))) // 2)