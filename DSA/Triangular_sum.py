# Problem Link: https://leetcode.com/problems/find-triangular-sum-of-an-array/description/?envType=daily-question&envId=2025-09-29

# Method-1: Brute Force
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n-1):
            # print(nums)
            for j in range(n-i-1):
                nums[j]=(nums[j]+nums[j+1])%10
        
        
        return nums[0]


# Method-2: Combinatrics
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def nCr(n, r): #not used
            ans=1
            for i in range(1, r+1):
                ans = (ans*(n-i+1))//i
            return ans

        n=len(nums)
        ans=0
        c=1
        for i in range(n):
            # print(nums[i], nCr(n-1, i))
            
            ans+=(nums[i]*c)%10
            c=(c*(n-1-i))//(i+1)
        
        return ans%10

# 1 2 3
# 3 5
# 8-> 1 + 2*2 + 3

# 1 2 3 4
# 3 5 7 
# 8 12
# 20 -> (1+2) + (2+3)*2 + (3+4) -> 1 + 2*3 + 3*3 + 4

# 1 2 3 4 5
# 3 5 7 9
# 8 12 16
# 20 28
# 48 -> (1+2) + (2+3)*3 + (3+4)*3 + (4+5) -> 1 + 2*4 + 3*6 + 4*4 + 5

# 4C0=1
# 4C1=4 
# 4C2=6
# 4C3=4
# 4C4=1

# nCr(n, r):
# 10 9 8 7
# 1 2 3 4

# 4 3
# 1 2
