import random
import unittest

from lab1.task14.src.max_value_of_expression import max_value_of_expression
from lab1.task14.src.naive import max_value_of_expression_naive


def get_random_expression() -> str:
    length = 5
    operators = random.choices('+-*', k=length - 1)
    numbers = random.choices('0123456789', k=length)
    return ''.join(numbers[i] + operators[i] for i in range(length - 1)) + numbers[length - 1]


class TestMaximizeGold(unittest.TestCase):
    def test_task_case(self):
        expression = "5-8+7*4-8+9"
        expected = 200
        self.assertEqual(max_value_of_expression(expression), expected)

    def test_smaller_expression(self):
        expression = "4+1*3*2-7"
        expected = 23
        self.assertEqual(max_value_of_expression(expression), expected)

    def test_larger_expression(self):
        expression = "1+1+1-1*2*3+1*2-2"
        expected = 30
        self.assertEqual(max_value_of_expression(expression), expected)

    def test_random_expression(self):
        expression = get_random_expression()
        expected = max_value_of_expression_naive(expression)
        self.assertEqual(max_value_of_expression(expression), expected)

    def test_largest_expression(self):
        expression = "4-8-5+1-3+2*0*2*1+0*2-3+5+7+9"
        expected = 598
        self.assertEqual(max_value_of_expression(expression), expected)


if __name__ == '__main__':
    unittest.main()
