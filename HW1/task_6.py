def sum_digit(n):
    sum = 0
    while n:
        sum, n = sum + n % 10, n // 10
    return sum

number = int(input())
print(('no', 'yes')[sum_digit(number % 1000) == sum_digit(number // 1000)])
