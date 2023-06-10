def print_operation_table(operation, num_rows=6, num_columns=6):
    [print(*[f'{operation(i + 1, j + 1):10}' for j in range(num_columns)]) for i in range(num_rows)]

print_operation_table(lambda x, y: x * y)
            