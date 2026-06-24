class rectangle_area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        self.area=self.length*self.breadth
        print("The area is calcuated")
    def display(self):
        print("Area of a rectangle is:",self.area)
s1=rectangle_area(10,7)
s1.area()
s1.display()
        