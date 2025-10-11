# Problem Link: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/?envType=daily-question&envId=2025-10-11
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        cump=power[:]
        ans=power[0]
        i,j=0,1
        mx=0
        while(j<len(power)):
            if(power[j-1]==power[j]):
                cump[j] = power[j]+cump[j-1]
                j+=1
                continue
            while(power[j]-power[i]>2):
                mx=max(mx, cump[i])
                i+=1
            if(i>0):
                cump[j] = power[j]+mx
            j+=1
        # print(power)
        # print(cump)
        ans=max(cump)
        return ans
