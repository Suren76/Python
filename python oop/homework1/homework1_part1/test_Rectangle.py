class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width

    def perimeter(self):
        self.perimeter = 2 * (self.length + self.width)

    def __repr__(self):
        return f"length:{self.length}, width:{self.width}"

    def __str__(self):
        return f"{(self.length).__str__()}, {(self.width).__str__()}"


rect = Rectangle(5, 6)

rect.area()
print(rect.area)

rect.perimeter()
print(rect.perimeter)

print(str(rect))

print(repr(rect))
