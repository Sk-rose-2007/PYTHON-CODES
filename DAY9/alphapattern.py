n=5
for i in range(1,n+1):
    print((n-i)*" ",end="")
    for j in range(1,i):
        print(chr(64+j),end="")
    for k in range(i,0,-1):
        print(chr(64+k),end="")
    print()
