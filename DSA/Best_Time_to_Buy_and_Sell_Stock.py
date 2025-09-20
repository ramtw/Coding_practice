#Problem link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min=prices[0]
        ans=0

        for p in prices[1:]:
            ans=max(ans, p-cur_min)
            cur_min=min(cur_min, p)
        return ans
