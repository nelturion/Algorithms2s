import unittest
from lab1.task14w.src.maximize_expression import max_value_of_expression, construct_expression


class TestMaxValueOfExpression(unittest.TestCase):
    def eval_expression(self, expr: str) -> int:
        return eval(expr)

    def test_single_element(self):
        sequence = [5]
        expected = 5
        max_val, operations = max_value_of_expression(sequence)
        expression = construct_expression(0, len(sequence) - 1, operations, sequence)
        self.assertEqual(max_val, expected)
        self.assertEqual(expression, "5")
        self.assertEqual(self.eval_expression(expression), max_val)

    def test_two_elements(self):
        sequence = [1, 2]
        expected = 3
        max_val, operations = max_value_of_expression(sequence)
        expression = construct_expression(0, len(sequence) - 1, operations, sequence)
        self.assertEqual(max_val, expected)
        self.assertEqual(self.eval_expression(expression), max_val)

    def test_three_elements(self):
        sequence = [1, 2, 3]
        expected = 9
        max_val, operations = max_value_of_expression(sequence)
        expression = construct_expression(0, len(sequence) - 1, operations, sequence)
        self.assertEqual(max_val, expected)
        self.assertEqual(self.eval_expression(expression), max_val)

    def test_different_order(self):
        sequence = [2, 3, 1]
        expected = 8
        max_val, operations = max_value_of_expression(sequence)
        expression = construct_expression(0, len(sequence) - 1, operations, sequence)
        self.assertEqual(max_val, expected)
        self.assertEqual(self.eval_expression(expression), max_val)

    def test_four_elements(self):
        sequence = [2, 1, 3, 4]
        expected = 36
        max_val, operations = max_value_of_expression(sequence)
        expression = construct_expression(0, len(sequence) - 1, operations, sequence)
        self.assertEqual(max_val, expected)
        self.assertEqual(self.eval_expression(expression), max_val)

    def test_complex_case(self):
        sequence = [3, 2, 5, 1, 4]
        max_val, operations = max_value_of_expression(sequence)
        expression = construct_expression(0, len(sequence) - 1, operations, sequence)
        self.assertEqual(self.eval_expression(expression), max_val)
        self.assertGreaterEqual(max_val, sum(sequence))


if __name__ == '__main__':
    unittest.main()