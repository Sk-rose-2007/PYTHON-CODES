try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    c=a/b
    print("The result of division is:", c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception:
    print("An error occurred")