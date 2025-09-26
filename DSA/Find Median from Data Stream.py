# Problem Link: https://leetcode.com/problems/find-median-from-data-stream/

# Method-1
class MedianFinder:

    def __init__(self):
        self.lheap=[]
        self.rheap=[]

    def addNum(self, num: int) -> None:
        if(not self.lheap):
            heapq.heappush(self.lheap, -1*num)
            return
        if(self.lheap[0]*-1 <= num):
            heapq.heappush(self.rheap, num)
        else:
            heapq.heappush(self.lheap, -1*num)
        
        while(len(self.rheap)>len(self.lheap)):
            x=heapq.heappop(self.rheap)
            heapq.heappush(self.lheap, -1*x)
        while(len(self.lheap)-len(self.rheap)>1):
            x=heapq.heappop(self.lheap)
            heapq.heappush(self.rheap, -1*x)
        
        
    def findMedian(self) -> float:
        # print(self.lheap)
        # print(self.rheap)
        s=len(self.lheap)+len(self.rheap)
        if(s%2==1):
            return self.lheap[0]*-1
        return ((-1*self.lheap[0])+self.rheap[0])/2
        

# Method-2
class MedianFinder:

    def __init__(self):
        self.lst=[]

    def addNum(self, num: int) -> None:
        if(not self.lst):
            self.lst.append(num)
            return
        i, j=0, len(self.lst)-1
        while(i<=j):
            m=(i+j)//2
            if(self.lst[m]==num):
                self.lst = self.lst[:m]+[num]+self.lst[m:]
                return
            if(self.lst[m]<num):
                i=m+1
            else:
                j=m-1
        
        self.lst = self.lst[:i]+[num]+self.lst[i:]
        return

    def findMedian(self) -> float:
        n=len(self.lst)
        if(n%2==1):
            return self.lst[n//2]
        return mean([self.lst[n//2], self.lst[(n//2)-1]])
