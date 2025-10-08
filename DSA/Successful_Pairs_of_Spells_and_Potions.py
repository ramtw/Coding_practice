# Problem Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=daily-question&envId=2025-10-08

# Method-I
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



# Mehtod-II
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        spell = 1 3 5
        potion = 1 2 3 4 5
        success = 7
        '''
        m=len(potions)
        n=len(spells)
        hep=[]
        for i in range(n):
            heappush(hep, (spells[i], i))

        potions.sort()
        print(potions)
        ans=[-1]*n

        def bs(x, i, j):
            # i=0
            # j=m-1
            while(i<=j):
                z=(i+j)//2
                if(potions[z]*x>=success):
                    j=z-1
                else:
                    i=z+1
            return j

        i, j = 0, m-1
        while(hep):
            s, ind = heappop(hep)
            x=bs(s, i, j)
            ans[ind] = max(m-1-x, 0)
            if(x>m-1):
                j=m-1
            elif(x<0):
                j=0
            else:
                j=x
        
        return ans


    
