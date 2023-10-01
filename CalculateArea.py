import math


class Shape:
    def area(self):
        raise NotImplementedError(f'Метод не реализован для класса {str(type(self).__name__)}')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid_triangle():
            raise ValueError(f'Треугольник {self.side1, self.side2, self.side3} недопустимый')

    def is_valid_triangle(self):
        return (self.side1 < self.side2 + self.side3 and
                self.side2 < self.side1 + self.side3 and
                self.side3 < self.side1 + self.side2)

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

    # def area(self):
    #     right_area = self.try_as_right_triangle()
    #     if right_area:
    #         return right_area
    #     p = (self.side1 + self.side2 + self.side3) / 2
    #     return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
    #
    # def try_as_right_triangle(self):
    #     sides = [self.side1, self.side2, self.side3]
    #     sides.sort()
    #     if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
    #         return sides[0] * sides[1] / 2
