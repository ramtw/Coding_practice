# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        # print(mp)
        heap=[]
        ans=[]

        for ky, v in mp.items():
            heapq.heappush(heap, (v,ky))
            if(len(heap)>k):
                heapq.heappop(heap)
        
        for x in heap:
            ans.append(x[1])
        return ans
