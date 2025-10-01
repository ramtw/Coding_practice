# Problem Link: https://leetcode.com/problems/water-bottles/?envType=daily-question&envId=2025-10-01

# Method-1
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        emptyB=numBottles

        while(emptyB>=numExchange):
            ans+=(emptyB//numExchange)
            emptyB = (emptyB//numExchange) + (emptyB%numExchange)

        return ans

# Method-2
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles)//(numExchange-1) - (numBottles%((numExchange-1))==0)

# Method-3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
