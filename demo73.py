class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    def max(self):
        return self.width * self.width + self.height * self.height


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 6)
r3 = Rectangle(7,11)
print r1.width, r1.height, r1.calculate_area()
print r2.width, r2.height, r2.calculate_area()
print r3.width, r3.height, r3.max()