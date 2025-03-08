from lab1.task14.src.process_data import read_data, write_data, validate_data


def calculate(num_1: int, operation: str, num_2: int) -> int:
    """
    Выполняет арифметическую операцию между двумя числами.
    """
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2


def max_value_of_expression(expression: list[str]) -> int:
    # количество чисел
    n = (len(expression) + 1) // 2

    numbers = [int(expression[2 * i]) for i in range(n)]
    operations = [expression[2 * i + 1] for i in range(n - 1)]

    mins = [[float('inf')] * n for _ in range(n)]
    maxs = [[-float('inf')] * n for _ in range(n)]

    for i in range(n):
        mins[i][i] = numbers[i]
        maxs[i][i] = numbers[i]

    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap

            # перебираем разбиения
            for k in range(i, j):
                op = operations[k]
                a = calculate(mins[i][k], op, mins[k + 1][j])
                b = calculate(mins[i][k], op, maxs[k + 1][j])
                c = calculate(maxs[i][k], op, mins[k + 1][j])
                d = calculate(maxs[i][k], op, maxs[k + 1][j])
                mins[i][j] = min(mins[i][j], a, b, c, d)
                maxs[i][j] = max(maxs[i][j], a, b, c, d)

    return maxs[0][n-1]


def main():
    input_path = '../files/input.txt'
    output_path = '../files/output.txt'
    expression = read_data(input_path)

    if not validate_data(expression):
        raise ValueError("Введите корректные данные")

    result = max_value_of_expression(expression)
    write_data(result, output_path)


if __name__ == '__main__':
    main()
