# Problem Link: https://leetcode.com/problems/find-triangular-sum-of-an-array/description/?envType=daily-question&envId=2025-09-29

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n-1):
            # print(nums)
            for j in range(n-i-1):
                nums[j]=(nums[j]+nums[j+1])%10
        
        
        return nums[0]
