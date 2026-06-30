arr=[1,2,3,4,3,2,6,7,5]
l={}
count=0
for i in arr:
    if i in l:
        l[i]=l[i]+1        
    else:
        l[i]=1
print(l)
for i,j in l.items():
    if j>1:
        count+=1
print(count)
