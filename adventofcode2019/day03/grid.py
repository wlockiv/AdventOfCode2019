class Grid:
    def __init__(self):
        self.grid = {}
        self.pos = (0, 0)
        self.__step_count = 0

    @property
    def points(self):
        return self.grid

    @property
    def step_count(self):
        return self.__step_count

    def step(self, direction):
        x, y = self.pos
        x_step = 1 if direction == 'R' else -1 if direction == 'L' else 0
        y_step = 1 if direction == 'U' else -1 if direction == 'D' else 0
        next_pos = (x + x_step, y + y_step)

        self.__step_count += 1
        # Use setdefault instead?
        # self.grid.setdefault(next_pos, self.__step_count)
        if next_pos not in self.grid:
            self.grid[next_pos] = self.__step_count
        self.pos = next_pos

    def walk(self, direction, dist):
        for step in range(1, dist + 1):
            self.step(direction)

    def walk_to_target(self, direction, dist, target):
        for step in range(1, dist + 1):
            self.step(direction)
            if self.pos == target:
                return True
        return False

    @staticmethod
    def manhattan_dist(point_1, point_2):
        x_1, y_1 = point_1
        x_2, y_2 = point_2
        return abs(x_2 - x_1) + abs(y_2 - y_1)
