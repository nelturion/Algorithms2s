from lab1.task_14_bad.src.process_data import read_data, write_data, validate_data


def max_value_of_expression(sequence: list[int]) -> list[int, list]:
    """
    Вычисляет максимальное значение выражения и матрицу операций
    """
    n = len(sequence)
    dp = [[float('-inf')] * n for _ in range(n)]
    operations = [[None] * n for _ in range(n)]

    # отрезки из одного числа
    for i in range(n):
        dp[i][i] = sequence[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                # сложение
                sum_val = dp[i][k] + dp[k + 1][j]
                if sum_val > dp[i][j]:
                    dp[i][j] = sum_val
                    operations[i][j] = (k, '+')

                # умножение
                mul_val = dp[i][k] * dp[k + 1][j]
                if mul_val > dp[i][j]:
                    dp[i][j] = mul_val
                    operations[i][j] = (k, '*')

    return dp[0][n - 1], operations


def construct_expression(i: int, j: int, operations: list[list], sequence: list[int]) -> str:
    """
    Восстанавливает строковое представление выражения по матрице операций.
    """
    if i == j:
        return str(sequence[i])

    k, op = operations[i][j]
    left_expr = construct_expression(i, k, operations, sequence)
    right_expr = construct_expression(k + 1, j, operations, sequence)

    return f"({left_expr}{op}{right_expr})"


def main():
    input_path = '../files/input.txt'
    output_path = '../files/output.txt'
    sequence = read_data(input_path)

    if not validate_data(sequence):
        raise ValueError("Введите корректные данные")

    max_value, operations = max_value_of_expression(sequence)
    constructed_expression = construct_expression(0, len(sequence) - 1, operations, sequence)

    write_data(max_value, constructed_expression, output_path)


if __name__ == '__main__':
    main()
