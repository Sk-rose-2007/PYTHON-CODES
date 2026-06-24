class person:
    def details(self):
        print("I am a human bieng")
class student(person):
    def declare(self):
        print("I am a student")
s1=student()
s1.details()
s1.declare()