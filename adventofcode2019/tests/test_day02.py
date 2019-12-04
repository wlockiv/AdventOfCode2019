import unittest

from adventofcode2019.day02 import part1, part2


class TestDay02(unittest.TestCase):
    def test_part1(self):
        test_values = {
            '1,0,0,0,99': 2,
            '2,3,0,3,99': 2,
            '2,4,4,5,99,0': 2,
            '1,1,1,4,99,5,6,0,99': 30
        }
        for k, v in test_values.items():
            self.assertEqual(part1.solve(k, noun=None, verb=None), v)

    # part 2 is impossible to test


if __name__ == '__main__':
    unittest.main()
