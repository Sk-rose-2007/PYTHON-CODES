def divisible(a):
    if  a % 3 == 0 and a % 8 == 0:
        print(a,"is divisible by both 3 and 8")
    elif a % 3 == 0:
        print(a,"is divisible by 3")
    elif a % 8 == 0:
        print(a,"is divisible by 8")
    else:
        print(a,"is not divisible by both 3 and 8")
divisible(int(input("Enter a number: ")))