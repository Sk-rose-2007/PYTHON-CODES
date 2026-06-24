students = []

for i in range(5):
    student = {}
    student["name"] = input("Enter Name: ")
    student["age"] = int(input("Enter Age: "))
    student["mark"] = int(input("Enter Mark: "))
    
    students.append(student)

print("\nStudent Details:")
for i in students:
    print("Name:", i["name"], "Age:", i["age"], "Mark:", i["mark"])