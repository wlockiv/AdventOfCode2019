import unittest

from adventofcode2019.day01 import part1, part2


class TestDay01(unittest.TestCase):
    def test_part1(self):
        test_values = {'12': 2, '14': 2, '1969': 654, '100756': 33583}
        for k, v in test_values.items():
            self.assertEqual(part1.solve(k), v)

    def test_part2(self):
        test_values = {'14': 2, '1969': 966, '100756': 50346}
        for k, v in test_values.items():
            self.assertEqual(part2.solve(k), v)


if __name__ == '__main__':
    unittest.main()
