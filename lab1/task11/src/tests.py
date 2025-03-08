import unittest
from lab1.task11.src.maximize_gold import maximize_gold


class TestMaximizeGold(unittest.TestCase):
    def test_all_fit(self):
        capacity = 10
        weights = [5, 5]
        expected = 10
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_greedy_not_optimal(self):
        capacity = 10
        weights = [6, 5, 5]
        expected = 6
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_multiple_small(self):
        capacity = 10
        weights = [3, 3, 3, 3]
        expected = 9
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_single_exact(self):
        capacity = 5
        weights = [5]
        expected = 5
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_single_too_big(self):
        capacity = 5
        weights = [6]
        expected = 0
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_combination_after_larger(self):
        capacity = 7
        weights = [4, 4, 3]
        expected = 7
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_all_same_large(self):
        capacity = 9
        weights = [5, 5, 5]
        expected = 5
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_greedy_better_than_optimal(self):
        capacity = 12
        weights = [9, 7, 4]
        expected = 9
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_sum_after_smaller(self):
        capacity = 10
        weights = [7, 3, 3, 3]
        expected = 10
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_no_better_combination(self):
        capacity = 10
        weights = [8, 7, 5]
        expected = 8
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_small_weights(self):
        capacity = 10
        weights = [1] * 300
        expected = 10
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_zero_weights(self):
        capacity = 10
        weights = [0, 0, 0]
        expected = 0
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_mixed_with_zero(self):
        capacity = 10
        weights = [10, 0, 0]
        expected = 10
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_large_weights(self):
        capacity = 10000
        weights = [100000] * 300
        expected = 0
        self.assertEqual(maximize_gold(capacity, weights), expected)

    def test_maximum_input(self):
        # Тест на предельные значения входных данных:
        # capacity максимальный = 10^4
        # n максимальное = 300
        n = 300
        capacity = 10 ** 4
        weights = [1] * n
        expected = 300
        self.assertEqual(maximize_gold(capacity, weights), expected)


if __name__ == '__main__':
    unittest.main()
