class school:
    school_name="TPMS"
    def __init__(self, name, age):
        self.name=name
        self.age=age
    @classmethod
    def display(cls):
        print("School Name:", cls.school_name)
s1=school(input("Enter Name: "), int(input("Enter Age: ")))
print("Name:",s1.name)
s1.display()