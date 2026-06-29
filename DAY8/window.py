nums=[1,3,2,5,4]
k=2
for i in range(len(nums)-k+1):
    print(max(nums[i:i+k]),end=" ")