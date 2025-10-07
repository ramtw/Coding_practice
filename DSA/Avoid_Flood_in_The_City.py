# Problem Link: https://leetcode.com/problems/avoid-flood-in-the-city/description/?envType=daily-question&envId=2025-10-07

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dh=[]
        fill={}
        ans=[-1]*len(rains)

        for i, l in enumerate(rains):
            if(l==0):
                # heappush(dh, i)
                dh.append(i)
                ans[i]=1
            else:
                if(l in fill and fill[l]!=-1):
                    j = bisect.bisect_left(dh, fill[l])
                    if(j>=len(dh)):
                        return []
                    else:
                        t=dh.pop(j)
                        ans[t]=l
                fill[l]=i
        
        return ans
