import unittest

from adventofcode2019.day03 import part1, part2


class TestDay03(unittest.TestCase):
    def test_part1(self):
        test_values = {
            'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83': 159,
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7': 135
        }

        for k, v in test_values.items():
            self.assertEqual(part1.solve(k), v)

    def test_part2(self):
        test_values = {
            'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83': 610,
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7': 410
        }

        for k, v in test_values.items():
            self.assertEqual(part2.solve(k), v)


if __name__ == '__main__':
    unittest.main()
