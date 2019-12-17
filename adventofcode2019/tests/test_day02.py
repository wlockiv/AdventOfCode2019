import unittest

from adventofcode2019.day02._part1 import Day02P1 as Solution


class TestDay02(unittest.TestCase):
    def test_part1(self):
        test_values = {
            (1, 0, 0, 0, 99): [2, 0, 0, 0, 99],
            (2, 3, 0, 3, 99): [2, 3, 0, 6, 99],
            (2, 4, 4, 5, 99, 0): [2, 4, 4, 5, 99, 9801],
            (1, 1, 1, 4, 99, 5, 6, 0, 99): [30, 1, 1, 4, 2, 5, 6, 0, 99]
        }

        for k, v in test_values.items():
            self.assertEqual(Solution.run_all_instruction(list(k), noun=None, verb=None), v)



if __name__ == '__main__':
    unittest.main()
