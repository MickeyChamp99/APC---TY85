class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        r = 5
        print("Circle Area:", 3.14 * r * r)

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        print("Rectangle Area:", l * b)

class Triangle(Shape):
    def area(self):
        b = 10
        h = 5
        print("Triangle Area:", 0.5 * b * h)

c = Circle()
r = Rectangle()
t = Triangle()

c.area()
r.area()
t.area()