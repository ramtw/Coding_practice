# Problem Link: https://leetcode.com/problems/water-bottles-ii/?envType=daily-question&envId=2025-10-02

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def eq(n):
            a=numBottles
            r=numExchange-1
            return a-n*r-(n*(n-1))//2
        ans=numBottles
        l,r=0,numBottles
        while(l<=r):
            n=(l+r)//2
            f=eq(n)
            if(f==0):
                return numBottles+n-1
            if(f<0):
                r=n-1
            else:
                l=n+1
        # print(l, eq(l-1), eq(l), eq(l+1))
        # print(r, eq(r-1), eq(r), eq(r+1))
        return numBottles+r



# 13 6
# 13 - (6-1) = 13-5 = 8 --> 1
# 8 - (7-1) = 8-6 = 2 --> 1
# 2 - (8-1) = 2-7 = -5 --> 0 

# r, r+1, r+2, r+3, r+4
# a-r, a-2r-1, a-3r-3, a-4r-6, a-5r-10
# nr+n(n-1)/2 = 
# x = a-(nr+n(n-1)/2) = a-nr-n(n-1)/2
# x = a-nr+r+n-2
# x = (1-r)n+a-2
# n = (a-2)//(r-1)

# a=13, r=5
# 11//4 = 2
# 13-10-1=2

# a=10, r=2
# 8//1 

# 0,2,3,4,5,6,7,8
# 10, 


