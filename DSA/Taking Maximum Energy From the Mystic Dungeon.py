# Problem Link: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/?envType=daily-question&envId=2025-10-10
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        ans=-1*math.inf

        for i in range(k, n):
            energy[i] = max(energy[i], energy[i]+energy[i-k])
            
        for i in range(n-k, n):
            ans=max(ans, energy[i])
        # print(energy)
        return ans
