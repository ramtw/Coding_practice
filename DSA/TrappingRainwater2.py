# Problem Link: https://leetcode.com/problems/trapping-rain-water-ii/description/?envType=daily-question&envId=2025-10-03

class Solution:
    def trapRainWater(self, hMap: List[List[int]]) -> int:
        m=len(hMap)
        n=len(hMap[0])
        ans=0

        pq = []
        visited=[]
        for i in range(m):
            rv=[0]*n
            visited.append(rv)

        for c in range(n):
            heappush(pq, (hMap[0][c], 0, c))
            visited[0][c]=1

            heappush(pq, (hMap[m-1][c], m-1, c))
            visited[m-1][c]=1

        for r in range(1, m-1):
            heappush(pq, (hMap[r][0], r, 0))
            visited[r][0]=1

            heappush(pq, (hMap[r][n-1], r, n-1))
            visited[r][n-1]=1

        # print(visited)
        rd=[-1, 1, 0, 0]
        cd=[0, 0, -1, 1]
        while(pq):
            t = heappop(pq)
            # print(t)
            for i in range(4):
                x = t[1]+rd[i]
                y = t[2]+cd[i]
                if(x<0 or x>=m or y<0 or y>=n or visited[x][y]==1):
                    # print(x, y)
                    continue
                # print(x, y)
                h = max(hMap[x][y], t[0])
                ans+=(h-hMap[x][y])
                # print(x, y, hMap[x][y], t[0])
                heappush(pq, (h, x, y))
                visited[x][y]=1

        return ans
