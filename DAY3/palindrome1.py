def palindrome1(x):
    if x<0:
        print("Invalid Number")
    original=x
    rev=0
    while x>0:
        digit=x%10
        rev=rev*10+digit
        x//=10
    if original==rev:
        print("It is palindrome") 
    else:
        print("Not a palindrome")
palindrome1(int(input()))