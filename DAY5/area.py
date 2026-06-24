class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        c = 3.14 * self.radius * self.radius
        print("Area of Circle:", c)
r1=circle(int(input("Enter Radius: ")))
r1.area()