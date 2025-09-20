#Problem link- https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0):
            return 0
        amt_set=set({0})
        lst=[0]
        ans=0

        while lst:
            ans+=1
            tmp=[]
            for amt in lst:
                for c in coins:
                    new_amt = c+amt
                    if(new_amt==amount):
                        return ans
                    if new_amt not in amt_set and new_amt<amount:
                        tmp.append(new_amt)
                        amt_set.add(new_amt)
            lst=tmp[:]

        return -1

        
