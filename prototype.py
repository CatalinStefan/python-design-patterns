import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        print(f"Drawing a square of size {self.size}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle of radius {self.radius}")


class AbstractArt:
    def __init__(self, bg_color, shapes):
        self.bg_color = bg_color
        self.shapes = shapes

    def draw(self):
        print(f"Background color is {self.bg_color}")
        [x.draw() for x in shapes]


if __name__ == '__main__':
    shapes = [Square(5), Square(3), Circle(8)]
    art1 = AbstractArt("red", shapes)

    art2 = copy.copy(art1)
    art1.draw()
    art2.draw()