n=5
j=n//2
for i in range(n+1):
    if i<=j+1:
        print("*"*i)
    else:
        print("*"*j)
        j-=1