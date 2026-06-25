class shape:
    def area(self):
        print("Calculating the area of the shape.")
class circle(shape):
    def area(self):
        print("The area of the circle is calculated.")
class rectangle(shape):
    def area(self):
        print("The area of the rectangle is calculated.")

shape1 = circle()
shape2 = rectangle()
shape1.area()
shape2.area()
  