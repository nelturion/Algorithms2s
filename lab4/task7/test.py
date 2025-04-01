import unittest

from lab4.task7.src.longest_substring import longest_common_substring


class TestLongestCommonSubstring(unittest.TestCase):
    def test_example_1(self):
        s = "abcdef"
        t = "zabcf"
        expected = (0, 1, 3)
        self.assertEqual(longest_common_substring(s, t), expected)

    def test_no_common_substring(self):
        s = "abc"
        t = "def"
        expected = (0, 0, 0)
        self.assertEqual(longest_common_substring(s, t), expected)

    def test_identical_strings(self):
        s = "hello"
        t = "hello"
        expected = (0, 0, 5)
        self.assertEqual(longest_common_substring(s, t), expected)

    def test_partial_overlap(self):
        s = "abcdxyz"
        t = "xyzabcd"
        expected = (0, 3, 4)
        self.assertEqual(longest_common_substring(s, t), expected)

    def test_empty_string(self):
        s = ""
        t = "nonempty"
        expected = (0, 0, 0)
        self.assertEqual(longest_common_substring(s, t), expected)

    def test_both_empty(self):
        s = ""
        t = ""
        expected = (0, 0, 0)
        self.assertEqual(longest_common_substring(s, t), expected)


class TestLongestCommonSubstringBoundary(unittest.TestCase):
    def test_maximum_values(self):
        # Здесь формируем две по 50000 символов
        s = "a" * 50000 + "b"
        t = "a" * 50000 + "c"
        expected = (0, 0, 50000)
        self.assertEqual(longest_common_substring(s, t), expected)


if __name__ == "__main__":
    unittest.main()
