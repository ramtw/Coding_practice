# Problem Link: https://leetcode.com/problems/find-median-from-data-stream/

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
