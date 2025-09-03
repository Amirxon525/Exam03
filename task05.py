class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14 
        return pi * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)
print(c.area()) 
print(r.area())   
