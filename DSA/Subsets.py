# Problem Link: https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        
        for x in nums:
            n=len(ans)
            for i in range(n):
                l=ans[i]
                t=ans[i][:]
                t.append(x)
                ans.append(t)

        return ans
