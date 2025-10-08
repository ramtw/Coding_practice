# Problem Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=daily-question&envId=2025-10-08

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        spell = 5 1 3
        potion = 1 2 3 4 5
        success = 7
        '''
        m=len(potions)
        n=len(spells)
        potions.sort()
        print(potions)
        ans=[]

        def bs(x):
            i=0
            j=m-1
            while(i<=j):
                z=(i+j)//2
                if(potions[z]*x>=success):
                    j=z-1
                else:
                    i=z+1
            return j

        for x in spells:
            i=bs(x)
            ans.append(max(m-1-i, 0))
        
        return ans
        

        
