number, sum = int(input()), 0
while number:
    sum, number = sum + number % 10, number // 10
print(sum)