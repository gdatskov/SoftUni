import math


class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        # return math.pi * self.radius ** 2
        return Circle.pi * self.radius ** 2

    def get_circumference(self):
        # return 2 * math.pi * self.radius
        return 2 * Circle.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
