# Problem Link: https://www.geeksforgeeks.org/problems/attend-all-meetings-ii/1

import heapq
class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        start.sort()
        end.sort()
        
        ans=0
        e=0
        for s in start:
            if(s<end[e]):
                ans+=1
            else:
                e+=1
        
        return ans
