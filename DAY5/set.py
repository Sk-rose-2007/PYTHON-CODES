students = set()

for i in range(5):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    mark = int(input("Enter Mark: "))

    students.add((name, age, mark))

print("\nStudent Details:")
for i in students:
    print("Name:", i[0], "Age:", i[1], "Mark:", i[2])