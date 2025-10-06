# Problem Link: https://leetcode.com/problems/swim-in-rising-water/?envType=daily-question&envId=2025-10-06

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ans=math.inf

        visit=[]
        for i in range(n):
            t=[0]*n
            visit.append(t)

        @cache
        def dfs(i,j,t):
            nonlocal ans
            if(i==n-1 and j==n-1):
                ans=min(ans, t)
                return

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                
                if(x<0 or y<0 or x>=n or y>=n or visit[x][y]==1):
                    continue
                visit[x][y]=1
                dt = max(0, grid[x][y]-t, grid[i][j]-t)
                dfs(x, y, t+dt)
                visit[x][y]=0
            return
        
        dfs(0, 0, 0)
        return ans
