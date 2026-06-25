class marksException(Exception):
    pass
try:
    marks = int(input("Enter your mark (out of 100): "))
    if marks < 0 or marks > 100:
        raise marksException("Marks should be between 0 and 100.")
    print("Your mark is:", marks)
except marksException as e:
    print("Error:", e)