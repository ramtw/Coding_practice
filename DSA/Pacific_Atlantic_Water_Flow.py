# Problem Link: https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=daily-question&envId=2025-10-05

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])

        pvisit=[]
        avisit=[]

        aq=deque()
        pq=deque()

        for i in range(m):
            ptmp=[0]*n
            atmp=[0]*n
            pvisit.append(ptmp)
            avisit.append(atmp)
            for j in range(n):
                if(i==0 or j==0):
                    pq.append((i,j))
                    pvisit[i][j]=1
                if(i==m-1 or j==n-1):
                    aq.append((i,j))
                    avisit[i][j]=1
                
        def bfs(que, visit):
            while(que):
                t=que.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = t[0]+dx, t[1]+dy
                    if(x<0 or y<0 or x>=m or y>=n or visit[x][y]==1 or heights[x][y]<heights[t[0]][t[1]]):
                        continue
                    
                    que.append((x,y))
                    visit[x][y]=1
        

        bfs(pq, pvisit)
        bfs(aq, avisit)

        ans=[]
        for i in range(m):
            for j in range(n):
                if(pvisit[i][j]==1 and avisit[i][j]==1):
                    ans.append([i,j])
        
        return ans
