def reverse(x):
    x = abs(x)
    rev = 0

    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit
        x //= 10
    print("Reverse of anumber is:",rev)
reverse(int (input("Enter a number: ")))
