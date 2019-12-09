import os

from adventofcode2019.solution import Solution


class Day08P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day08P1, self).__init__(input_file, test_input=test_input)

    @staticmethod
    def parse_raw(raw_input):
        return list(raw_input)

    @property
    def solution(self):
        pixels = self.parsed_input.copy()
        img_w, img_h = 25, 6
        num_layers = len(pixels) // (img_w * img_h)
        layers = [ImageLayer(img_w, img_h) for _ in range(num_layers)]
        val_counts = [[], [], []]
        for layer in layers:
            for _ in range(layer.height):
                layer.add_pixel_row(pixels[:layer.width])
                del pixels[:layer.width]
            [val_counts[p].append(layer.get_val_count(p)) for p in range(len(val_counts))]

        min_zeros_index = val_counts[0].index(min(val_counts[0]))
        return val_counts[1][min_zeros_index] * val_counts[2][min_zeros_index]


class ImageLayer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pixel_rows = []

    def __is_full(self):
        return len(self.pixel_rows) == self.height

    def get_val_count(self, val: int):
        return [p for pr in self.pixel_rows for p in pr].count(val)

    def add_pixel_row(self, pixels: list):
        if (input_len := len(pixels)) != self.width:
            raise Exception(f'Pixel row does match image width. {self.width=}, {input_len=}')
        if self.__is_full():
            raise Exception(f'This image is already full. Cannot add any more pixels.')

        self.pixel_rows.append([int(p) for p in pixels])


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day08P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 08: Part 1')
    print(f'\tSolution: {solve()}')
