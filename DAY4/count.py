l=[1,2,3,4,5,6,7,8,9,10]
evencount=0
oddcount=0
for i in l:
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1 
print("Even count =", evencount)
print("Odd count =", oddcount)