import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

    # <
    def __lt__(self, other):
        return self.radius < other.radius

    # <=
    def __le__(self, other):
        return self.radius <= other.radius

    # ==
    def __eq__(self, other):
        return self.radius == other.radius

    # !=
    def __eq__(self, other):
        return self.radius != other.radius

    # >=
    def __ge__(self, other):
        return self.radius >= other.radius

    # >
    def __gt__(self, other):
        return self.radius > other.radius

    def __add__(self, other):
        self.radius += other.radius
        return self

    def __sub__(self, other):
        self.radius -= other.radius
        return self
