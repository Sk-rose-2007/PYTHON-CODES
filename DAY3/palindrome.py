class Solution(object):
    def Palindrome(self, x):
        if x<0:
            return False
        original=x
        rev=0
        while x>0:
            digit =x%10
            rev=rev*10+digit
            x=x//10
        
        if x<-2**31 or x>2**31-1:
            return 0
        return original==rev
print(Solution().Palindrome(int(input())))      