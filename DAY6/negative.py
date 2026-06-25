class negativeException(Exception):
    pass
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise negativeException("Negative numbers are not allowed.")
    print("Your number:", num)
except negativeException as e:
    print("Use positive number,", e)
