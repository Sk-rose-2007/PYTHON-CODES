l=[1,2,3,4,5,6,7,8,9,10]
even=[]
od=[]
for i in range(len(l)):
    if l[i]%2==0:
        even.append(l[i])
    else:
        od.append(l[i])
print("even list:",even)
print("odd list:",od)
