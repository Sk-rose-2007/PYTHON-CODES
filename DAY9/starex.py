n=5
b=1
a=((n*2)-1)//2
for i in range(n,0,-1):
    if i==n:
       print("*"*((n*2)-1))
    else:
        print("*"*i," "*b+"*"*i)
        b+=2
