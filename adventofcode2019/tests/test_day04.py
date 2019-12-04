import unittest

from adventofcode2019.day04 import part1, part2


class TestDay04(unittest.TestCase):
    def test_part1(self):
        test_values = {'111111': 1, '223450': 0, '123789': 0}
        for k, v in test_values.items():
            self.assertEqual(part1.solve(k), v)

    def test_part2(self):
        test_values = {'112233': 1, '123444': 0, '111122': 1}
        for k, v in test_values.items():
            self.assertEqual(part2.solve(k), v)


if __name__ == '__main__':
    unittest.main()
