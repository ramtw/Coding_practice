# Problem Link: https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp={}
        for x in prerequisites:
            if x[0] in mp:
                mp[x[0]].append(x[1])
            else:
                mp[x[0]]=[x[1]]
        
        visited=[0]*numCourses
        dp = [0]*numCourses
        def dfs(n):
            if(visited[n]==1):
                return False
            
            if(dp[n]==1):
                return True
            visited[n]=1
            for c in mp.get(n, []):
                if(dfs(c)==False):
                    return False
            visited[n]=0
            dp[n]=1
            return True
        
        for k,v in mp.items():
            if(dfs(k)==False):
                return False
        return True


# 1->2->3->4
#       |
#       v
#       5->6->7->1
#       |
#       v
#       8->9->10
