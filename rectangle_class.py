import random
import pygame

WIDTH = 600
HEIGHT = 350

total_rects = 20
x_list = [x for x in range(100, (WIDTH - 100)) if x % (((WIDTH - 100) - 100) // total_rects) == 0]
h_list = random.sample(range(50, 200), total_rects)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
NAVY = (26, 55, 77)
DARK_BLUE = (64, 104, 130)
BLUE = (105, 152, 171)
LIGHT_BLUE = (177, 208, 224)
blue_list = [NAVY, DARK_BLUE, BLUE, LIGHT_BLUE]

class Rectangle():

    def __init__(self):
        self.color = self.get_color(blue_list)
        self.width = ((WIDTH - 100) - 100) / total_rects
        self.height = self.get_height()
        self.x = self.get_x(x_list)
        self.y = HEIGHT - self.height

    def get_x(self, xs):
        x = xs[0]
        xs.remove(x)
        xs.append(x)

        return x

    def get_color(self, colors):
        col = colors[0]
        colors.remove(col)
        colors.append(col)
        return col

    def get_height(self):
        return random.randint(50, 200)

    def make_sorting(self):
        self.color = GREEN

    def make_comparing(self):
        self.color = RED    

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
        
def make_rects():
    rect_row = []

    for i in range(total_rects):
        i = Rectangle()
        rect_row.append(i)

    return rect_row