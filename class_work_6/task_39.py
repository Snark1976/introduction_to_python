mas1, mas2 = list(map(int, input().split())), list(map(int, input().split()))
print([i for i in mas1 if i not in mas2])