n=3
counter=n*(n+1)//2
for i in range(n,0,-1):
    for j in range(i):
        print(counter,end=" ")
        counter-=1
    print()