import unittest

from lab3.task11.src.alchemy import process_substances


class TestProcessSubstances(unittest.TestCase):
    def test_example_1(self):
        input_moves = [
            "Aqua -> AquaVita",
            "AquaVita -> PhilosopherStone",
            "AquaVita -> Argentum",
            "Argentum -> Aurum",
            "AquaVita -> Aurum"
        ]
        start = "Aqua"
        target = "Aurum"
        expected = 2
        self.assertEqual(process_substances(input_moves, start, target), expected)

    def test_example_2(self):
        input_moves = [
            "Aqua -> AquaVita",
            "AquaVita -> PhilosopherStone",
            "AquaVita -> Argentum",
            "Argentum -> Aurum",
            "AquaVita -> Aurum"
        ]
        start = "Aqua"
        target = "Osmium"
        expected = -1
        self.assertEqual(process_substances(input_moves, start, target), expected)

    def test_direct_conversion(self):
        input_moves = ["Water -> Steam"]
        start = "Water"
        target = "Steam"
        expected = 1
        self.assertEqual(process_substances(input_moves, start, target), expected)

    def test_no_moves(self):
        input_moves = []
        start = "Gold"
        target = "Silver"
        expected = -1
        self.assertEqual(process_substances(input_moves, start, target), expected)

    def test_cycle(self):
        input_moves = [
            "A -> B",
            "B -> C",
            "C -> A",
            "C -> D"
        ]
        start = "A"
        target = "D"
        expected = 3
        self.assertEqual(process_substances(input_moves, start, target), expected)


class TestProcessLotsOfSubstances(unittest.TestCase):
    def test_maximum_values(self):
        # Формируем цепочку S1 -> S2, S2 -> S3, ..., S99 -> S100 (99 реакций)
        chain = [f"S{i} -> S{i + 1}" for i in range(1, 100)]

        extra_moves = []
        for i in range(901):
            substance = f"S{(i % 100) + 1}"
            extra_moves.append(f"{substance} -> {substance}")

        input_moves = chain + extra_moves

        start = "S1"
        target = "S100"
        expected = 99

        result = process_substances(input_moves, start, target)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")


if __name__ == "__main__":
    unittest.main()
