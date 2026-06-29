s=["h","e","l","l","o"]
l=[]
y=len(s)
a=s[::-1]
for i in range(y):
    for j in range(a,0,-1):
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
        l.append(temp)
print(l)