class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.141592653589793 * self.radius

c = Circle(5)
print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
