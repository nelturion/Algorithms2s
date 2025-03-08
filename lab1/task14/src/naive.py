def generate_parentheses(expression):
    if len(expression) <= 1:
        return [expression]

    results = set()
    for i in range(1, len(expression), 2):  # перебираем операторы
        left_expressions = generate_parentheses(expression[:i])
        right_expressions = generate_parentheses(expression[i + 1:])

        for left in left_expressions:
            for right in right_expressions:
                results.add(f'({left}{expression[i]}{right})')

    return results


def find_max_expression_value(expression):
    expressions = generate_parentheses(expression)
    max_value = float('-inf')
    max_expr = ""

    for expr in expressions:
        value = eval(expr)
        if value > max_value:
            max_value = value
            max_expr = expr

    return max_value, max_expr

def max_value_of_expression_naive(expression):
    max_value, max_expr = find_max_expression_value(expression)
    return max_value
