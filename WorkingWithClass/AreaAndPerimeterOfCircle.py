import math


class Circle:
    def __init__(self, radius=2):
        self.radius = radius

    def area(self):
        return self.radius * math.pi

    def perimeter(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius



# myCircle = Circle()
# print(myCircle.area())
# print(myCircle.perimeter())
# myCircle.setRadius(5)
# print(myCircle.area())
# print(myCircle.perimeter())
