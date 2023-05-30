max_number = -1
while (n := int(input())) != 0:
    if max_number < n:
        max_number = n
print(max_number)