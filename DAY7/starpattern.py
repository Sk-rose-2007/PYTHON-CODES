n=3
a=1
for i in range(1,n+1):
    for j in range(i,n):
        print(" ", end="")
    for k in range(i,i+1):
        print("*"*a)
        a+=2
