# Problem Link: https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        m=len(grid)
        n=len(grid[0])
        r=[-1, 1, 0, 0]
        c=[0, 0, -1, 1]
        
        def fun(i, j):
            grid[i][j]='0'
            for k in range(4):
                x, y = i+r[k], j+c[k]
                if(not(x<0 or x>=m or y<0 or y>=n or grid[x][y]=='0')):
                    fun(x, y)

        for i in range(m):
            for j in range(n):
                if(grid[i][j]=='1'):
                    ans+=1
                    fun(i,j)
        return ans
        
