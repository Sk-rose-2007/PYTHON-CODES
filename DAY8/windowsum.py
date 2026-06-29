nums=[1,3,4,5,2]
k=3
a=[]
for i in range(len(nums)-k+1):
    a.append(sum(nums[i:i+k]))
print(max(a))


