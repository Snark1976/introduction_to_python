import random
n, x = int(input()), int(input())
lst = [random.randint(0, 10) for _ in range(n)]
print(lst, sum(x == i for i in lst), sep='\n')
