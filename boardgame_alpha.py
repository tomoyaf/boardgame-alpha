import numpy as np

class BoardgameAlpha:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.turn = True
        self.field = np.array([
            np.array([(x + y) % 2 == 0 for x in range(width)]) for y in range(height)
        ])
        print(self.get_turn())
        print(self.get_field())

    def update(self, x, y):
        if not self.check_input(x, y):
            return False
        self.flip(x, y)
        self.turn = not self.turn
        return True

    def flip(self, x, y):
        for xi in [-1, 0, 1]:
            for yi in [-1, 0, 1]:
                self.field[y + yi][x + xi] = not self.field[y + yi][x + xi]
        print(self.get_turn())
        print(self.get_field())

    def check_input(self, x, y):
        return  x >= 0 and x < self.width and y >= 0 and y < self.height

    def get_turn(self):
        return self.turn

    def get_field(self):
        return 1.0 * self.field
