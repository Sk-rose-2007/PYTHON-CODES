class Solution(object):
    def findDuplicate(self, nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value>1:
                return key
s1=[1,2,3,4,5,2]
a=Solution()
print(a.findDuplicate(s1))