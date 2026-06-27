n=6
for i in range(1,n+1):
        if(i==n or i==1):
            print("*"*n,end="")
        else:
            print("*"+" "*(n-2)+"*",end="")
        print()