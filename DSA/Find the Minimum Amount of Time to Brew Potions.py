# Problem Link: https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/?envType=daily-question&envId=2025-10-09
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n=len(skill)
        m=len(mana)
        end = [0]*n
        end[0]=mana[0]*skill[0]
        for i in range(1, n):
            end[i]=end[i-1]+mana[0]*skill[i]
        # print(end)

        for j in range(1, m):
            s=end[-1]+1
            for w in range(n-2, -1, -1):
                s=max(s-skill[w]*mana[j], end[w]+1)
                # print(s, end=' ')
            # print()
            end[0]=s+skill[0]*mana[j]-1
            for w in range(1, n):
                end[w]=end[w-1]+skill[w]*mana[j]
            # print('end', end)

        return end[-1]


