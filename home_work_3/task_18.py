import random
n, x = int(input()), int(input())
lst = [random.randint(-100, 100) for _ in range(n)]
print(lst, sorted(((abs(x - i) * 10 - (i < x), i) for i in lst))[0][1], sep='\n')
# если есть пара равноудаленных от Х, то выводим меньшее