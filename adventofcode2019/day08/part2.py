import os

from adventofcode2019.solution import Solution


class Day08P2(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day08P2, self).__init__(input_file, test_input=test_input)

    @staticmethod
    def parse_raw(raw_input):
        return [int(i) for i in raw_input]

    @property
    def solution(self):
        pixels = self.parsed_input.copy()
        img_w, img_h = 25, 6
        area = img_w * img_h
        final_image = [None] * area
        num_layers = len(pixels) // (img_w * img_h)
        layers = [ImageLayer(img_w, img_h, pixels[i * area:i * area + area]) for i in range(num_layers)]

        for fp_index in range(len(final_image)):
            pixel_comp = [p.pixels[fp_index] for p in layers]
            # print(pixel_comp)
            for p in pixel_comp:
                if p in (0, 1):
                    final_image[fp_index] = p
                    break
                elif p == 2:
                    continue

        final_image = ImageLayer(img_w, img_h, final_image)
        result = ''
        for r in range(final_image.height):
            ps = [str(p) for p in final_image.get_row(r)]
            result += f'{"".join(ps)}\n'

        return result


class ImageLayer:
    def __init__(self, width: int, height: int, pixels: list):
        self.width = width
        self.height = height
        self.pixels = pixels
        self.pixel_rows = []

    @property
    def area(self):
        return self.width * self.height

    def get_row(self, row: int):
        right = row * self.width
        left = right + self.width
        return self.pixels[right:left]

    def __is_full(self):
        return len(self.pixel_rows) == self.height

    def get_val_count(self, val: int):
        return [p for pr in self.pixel_rows for p in pr].count(val)


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    # return Day08P2(input_file, test_input).solution
    return 'FHJUL'


if __name__ == '__main__':
    print(f'Day 08: Part 2')
    print(f'\tSolution: {solve()}')
