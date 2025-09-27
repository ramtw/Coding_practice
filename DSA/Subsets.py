# Problem Link: https://leetcode.com/problems/subsets/

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


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
